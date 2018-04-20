from geomet import wkt
import json

#questo programma permette di convertire le coordinate di un punto preso in input da google map
# e di convertirlo in formato wkt
#potete ottenere le coordinate di un punto a partire da una località a questo indirizzo
# http://www.mapcoordinates.net/it
a=[]
latitudine= 42.116667
longitudine= 14


a.append({
  "type": "Point",
  "coordinates": [
    longitudine,
    latitudine
  ]
})

b=wkt.dumps(a[0],decimals=7)

print(b)
