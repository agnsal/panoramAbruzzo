'''
Copyright 2018 Agnese Salutari, Alessia Di Fonso, Cecilia D'Amico.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License
'''

from __future__ import absolute_import, print_function
import sys

import json
import tweepy

class TweetMiner:
    # == OAuth Authentication ==
    # This mode of authentication is the new preferred way
    # of authenticating with Twitter.
    # The consumer keys can be found on your application's Details
    # page located at https://dev.twitter.com/apps (under "OAuth settings")
    __consumer_key = None
    __consumer_secret = None
    # The access tokens can be found on your applications's Details
    # page located at https://dev.twitter.com/apps (located
    # under "Your access token")
    __access_token = None
    __access_token_secret = None
    #auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    #auth.set_access_token(access_token, access_token_secret)
    #api = tweepy.API(auth)
    __auth = None
    __api = None
    __new_tweets = [] # New Tweets List

    def __init__(self, consumerKey = 'QMXeyomZpypPaWGKy2t8OvJSa',
                 consumerSecret = 'YvOsh7zIduR8wk61Ykqa6SJPFXk6Uuej7mCTi0NM5CVSYjFajK',
                 accessToken = '4876002904-hnuEcPr2geDcgTqoCjN5bm3xjEdnEf9N49jUEJ8',
                 accessTokenSecret = 'nHgdWjz5T8350xvmJUVOVjUMLlG4lkn2S1x1TjGVrbiZj'):
        assert isinstance(consumerKey, str)
        assert isinstance(consumerSecret, str)
        assert isinstance(accessToken, str)
        self.__consumer_key = consumerKey
        self.__consumer_secret = consumerSecret
        self.__access_token = accessToken
        self.__access_token_secret = accessTokenSecret
        self.__auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        self.__auth.set_access_token(accessToken, accessTokenSecret)
        self.__api = tweepy.API(self.__auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        if not self.__api:
            print("Can't Authenticate")
            sys.exit(-1)

    def writeHtml(self, content, htmlPath):
        assert isinstance(htmlPath, str)
        assert isinstance(content, str)
        out_file = open(htmlPath, "a")
        out_file.write('<table width="500" border="1" cellpadding="5"><tr><td align="center" valign="center"><img src="'+
                       content +
                        '" alt="description here" /><br />Caption text centered under the image.</td></tr></table>')
                        #<td align="center" valign="center"><img src=" '+image+
                        #'" alt="description here" /><br />Caption text centered under the image.</td>
                        # </tr></table>')
        out_file.close()

    def writeTxt(self, content, txtPath):
        assert isinstance(txtPath, str)
        assert isinstance(content, str)
        out_file = open(txtPath, "a")
        out_file.write(content + '\n')
        out_file.close()

    def mineTweetsByHashtag(self, searchQuery = '#abruzzo', tweetsXQry = 100):
    # Hashtag based Tweets search.
    #   searchQuery is the Tweets keyword;
    #   tweetsXQry is the max number of Tweets API is allowed to take.
        assert isinstance(searchQuery, str)
        assert isinstance(tweetsXQry, int)
        print('Mining Tweets by Hashtag...')
        self.__new_tweets = self.__api.search(q=searchQuery, count=tweetsXQry)
        print('Tweets found.')

    def mineTweetsByAccount(self, screenName = 'panoramAbruzzo', tweetsXQry = 200):
    # Account based Tweets search.
    #   screenName is the Twitter account to ask for Tweets;
    #   tweetsXQry is the max number of Tweets API is allowed to take.
        assert isinstance(screenName, str)
        print('Mining Tweets by Hashtag...')
        self.__new_tweets = self.__api.user_timeline(screen_name=screenName, count=tweetsXQry)
        print('Tweets found.')


    def showNewTweets(self, outHtmlPath = "newTweets.html", outTxtPath = "newTweets.txt"):
        assert isinstance(outHtmlPath, str)
        assert isinstance(outTxtPath, str)
        print('New Tweets:')
        print('************************************************')
        for i in range(len(self.__new_tweets)):
            json_Str = json.dumps(self.__new_tweets[i]._json)
            json_reply = json.loads(json_Str)
            # print(json_reply['text']) # Test
            self.writeTxt(json_Str, outTxtPath)
            if 'entities' in json_reply:
                if 'media' in json_reply['entities']:
                    print (json_reply ['entities']['media'])
                    # a = json.loads(json_reply['entities']['media']))
                    a = json_reply['entities']['media']
                    print(a[0]['media_url'])
                    self.writeHtml(a[0]['media_url'], outHtmlPath)
                    self.writeTxt(json.dumps(json_reply), outTxtPath)
                    print ('*********************************------*****************************************')
        print('*****************************************')