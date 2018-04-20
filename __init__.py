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

import TweetsMiner

def main():
    tm = TweetsMiner.TweetMiner(consumerKey = 'QMXeyomZpypPaWGKy2t8OvJSa',
                 consumerSecret = 'YvOsh7zIduR8wk61Ykqa6SJPFXk6Uuej7mCTi0NM5CVSYjFajK',
                 accessToken = '4876002904-hnuEcPr2geDcgTqoCjN5bm3xjEdnEf9N49jUEJ8',
                 accessTokenSecret = 'nHgdWjz5T8350xvmJUVOVjUMLlG4lkn2S1x1TjGVrbiZj')
    tm.mineTweetsByAccount(screenName = 'panoramAbruzzo', tweetsXQry = 200)
    tm.showNewTweets(outHtmlPath = "newTweets.html", outTxtPath = "newTweets.txt")


if __name__ == '__main__':
    main()


