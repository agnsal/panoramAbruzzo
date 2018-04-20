from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
from geomet import wkt

# Questo programma estrae le informazioni id;descrizione;url;posizione;località;tweet   dai tweet
#prende in input un file sorgente che contiene solo quei tweet che contengono le immagini e restituisce un file csv che può essere comodamente visualizzato in excel.

def writeHtml(imageUrl,caption):
 out_file = open("immaginiAbruzzoUpnDown2.html","a")
 out_file.write('<table width="500" border="1" cellpadding="5"><tr><td align="center" valign="center"><img src="'+ imageUrl +
                '" alt="description here" /><br />'+caption+'</td></tr></table>')
                #<td align="center" valign="center"><img src=" '+image+
                #'" alt="description here" /><br />Caption text centered under the image.</td>
                # </tr></table>')
 out_file.close()
 return

tweets_data = []
fileSorgenteImmagini = open("panoramAbruzzoImmagini.txt", "r")
for line in fileSorgenteImmagini:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
     #   print(tweet)   
    except:
        continue
i=0
tweet_id=[]
datiFoto=[]
posizione=[]
geoJson=[]
località=[]
text=[]
imgCount=0
tweetID=[]
tupla=[]
shapes=[]
fileCSV = open("panoramAbruzzo.csv","w+",encoding='utf8')
fileCSV.write("id;descrizione;url;posizione;località;tweet\n")   #scrive la prima riga con il nome dei campi- necessaria nel formato csv 

for count in tweets_data:
    tweet_id.append(tweets_data[i]['id'])
  # tweetID.append()


    if (tweets_data[i]['coordinates'] is not None):
                print('**********************************')
                print('queste sono le coordinate puntuali'+str(tweets_data[i]['coordinates']))

              #  geoJson.append(tweets_data[i]['coordinates'])
                shapes.append(wkt.dumps(tweets_data[i]['coordinates'],decimals=7))
                località.append(str(tweets_data[i]['place']['full_name']).replace(',',''))
   
        
            
    else:

            if tweets_data[i]['place'] is not None: 
            
                if 'bounding_box' in tweets_data[i]['place']:
                #    posizione.append(tweets_data[i]['place']['bounding_box']['coordinates'])
                 #   geoJson.append(str(tweets_data[i]['place']['bounding_box']).replace('\'', '"'))
                    #tweets_data[i]['place']['bounding_box']['coordinates'].append(tweets_data[i]['place']['bounding_box']['coordinates'][0][1]) #per aggiungere il 5° punto alla geometria del poligono
                    shapes.append(wkt.dumps(tweets_data[i]['place']['bounding_box'],decimals=7))  #questo va bene se i punti del poligono sono 4, se sono 5 la libreria non fa la conversione 
                    print('qui c\'è un polygon')
                    
                    if 'full_name' in tweets_data[i]['place']:
                        località.append(str(tweets_data[i]['place']['full_name']).replace(',',''))

                       # posizione.append('null')
                        
                   
            else:
                geoJson.append('null')
                shapes.append('null')
                località.append('null')
                print('qui non c\'è la posizione')
   # 
        

    if 'entities' in tweets_data[i]:
        if 'media' in tweets_data[i]['entities']:
       
            datiFoto.append(tweets_data[i]['entities']['media'])
            text.append((tweets_data[i]['text']).replace('\'', ''))
            
            imgCount+=1
    i+=1




for k in range(i):   

    fileCSV.write('\''+str(tweet_id[k])+'\';\''+text[k].replace(';', '')+'\';\''+ datiFoto[k][0]['media_url']+'\'; ST_GeomFromText( \''+shapes[k]+'\',43);\''+località[k]+'\';'+str(tweets_data[k])+'\n')
fileCSV.close()
  #  print("id: "+str(k) + ", descrizione: "+ text[k]+", url: " + datiFoto[k][0]['media_url']+ ", posizione: " + str(posizione[k])+ ", località: " +località[k])+"\n"))
