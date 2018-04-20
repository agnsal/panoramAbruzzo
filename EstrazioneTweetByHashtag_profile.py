from __future__ import absolute_import, print_function
import sys

import json
import os
import tweepy


def writeHtml(image):
 out_file = open("nuoveImm.html","a")
 out_file.write('<table width="500" border="1" cellpadding="5"><tr><td align="center" valign="center"><img src="'+ image +
                '" alt="description here" /><br />Caption text centered under the image.</td></tr></table>')
                #<td align="center" valign="center"><img src=" '+image+
                #'" alt="description here" /><br />Caption text centered under the image.</td>
                # </tr></table>')
 out_file.close()
 return


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

#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)

#api = tweepy.API(auth)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True,
				   wait_on_rate_limit_notify=True)

if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)

#hashtag='#abruzzo';
searchQuery = '#abruzzo'  # mettere qui la chiave di ricerca in base alla quale si vuole cercare i tweet
maxTweets = 100 #   numero di tweet che si vogliono scaricare 
tweetsPerQry = 100  # massimo numero permesso dall'API



#lista dei profili che abbiamo salvato

#screen_name='abruzzopassion'
#screen_name='YourAbruzzo'
#screen_name='abruzzo4foodies'
#screen_name='igers_abruzzo'
#screen_name='Vivilabruzzo'
#screen_name='abruzzoparks'
#screen_name='abruzzoborgo'
#screen_name='AbruzzoUpnDown'
#screen_name='lifeinabruzzo'
#screen_name='itineraridabruz'
#screen_name='paesaggiabruzzo'
#screen_name='majambiente'
#screen_name='natourarte_info'
#screen_name='parcomajella'
#screen_name='paesaggiabruzzo'
#screen_name='TerreTrabocchi'

screen_name='panoramAbruzzo'

#new_tweets = api.search(q=searchQuery, count=tweetsPerQry)   #scommentate se volete fare la ricerca in base all'hashtag
new_tweets = api.user_timeline(screen_name = screen_name,count=200)   #questa riga scarica la timeline di un utente

i=0;



print('************************************************')
imgCount=0  
a=[]
out_file = open("panoramAbruzzo.txt","a")            #mettere qui il nome del file da scrivere fino ad adesso ho usato la convenzione screenName.txt
out_file_imm=open("panoramAbruzzoImmagini.txt","w+")  # #mettere qui il nome del file da scrivere fino ad adesso ho usato la convenzione screenNameImmagini.txt

for count in new_tweets:
   json_Str=json.dumps(new_tweets[i]._json)
   json_reply = json.loads(json_Str)
  # print(json_reply['text'])

   out_file.write(json_Str+'\n')
  

 
   
   if 'entities' in json_reply:
      
       if 'media' in json_reply['entities']:
           print (json_reply ['entities']['media'])
        #   a.append(json.loads(json_reply ['entities']['media']))
           a.append(json_reply ['entities']['media'])
           out_file_imm.write(json.dumps(json_reply)+"\n")
                
       
           print ('*********************************------*****************************************')
    
           imgCount+=1
  
      
   i+=1


print('*****************************************')
out_file.close()
out_file_imm.close()
for i in range(len(a)):
    print(a[i][0]['media_url'])
    writeHtml(a[i][0]['media_url'])



                

sinceId = None

