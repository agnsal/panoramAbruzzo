from __future__ import absolute_import, print_function
import sys

import json
import os
import tweepy

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#questo programma estrae i tweet recenti in base a delle chiavi di ricerca specifiche




# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key='QMXeyomZpypPaWGKy2t8OvJSa'
consumer_secret='YvOsh7zIduR8wk61Ykqa6SJPFXk6Uuej7mCTi0NM5CVSYjFajK'


# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token='4876002904-hnuEcPr2geDcgTqoCjN5bm3xjEdnEf9N49jUEJ8'
access_token_secret='nHgdWjz5T8350xvmJUVOVjUMLlG4lkn2S1x1TjGVrbiZj'






class StdOutListener(StreamListener):

        
    def on_data(self, data):
        print (data)  #stampa i tweet che trova
       
        with open('nuovihashtag.txt','a') as tf:   #nome del file in cui si vogliono mettere i tweet
            tf.write(data)         #scrive i tweet trovati nel file
   #     self.writeOnFile(Data)
        return True

    def on_error(self, status):
        print (status)

    
 

if __name__ == '__main__':

    #autenticazione e connessione all'API Twitter
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #tra parentesi si devono mettere le chiavi di ricerca: 
    stream.filter(track=[ 'yallersabruzzo','loves_united_abruzzo', 'paesaggidabruzzo'])
    


