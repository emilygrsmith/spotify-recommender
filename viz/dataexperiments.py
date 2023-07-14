import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv
import os
from dotenv import load_dotenv

load_dotenv()



#Authentication - without user
client_credentials_manager = SpotifyClientCredentials(client_id=os.getenv('CLIENT_PUBLIC_KEY'), client_secret=os.getenv('CLIENT_SECRET_KEY'))
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)


artist = '06HL4z0CvFAxyc27GXpf02'
results = sp.artist_albums(artist)
album_ids = [results['items'][x]['id'] for x in range(len(results['items']))]

song_list = []
song_params = 0
for x in album_ids:
    song = sp.album_tracks(x, limit = 50)
   
    song_params = len(song)
   
    song_list.append(song)

song_individual = []
count = 0

#list of all songs

for x in range(len(song_list)):
    for y in range(len(song_list[x]['items'])):
        song_individual.append(song_list[x]['items'][y])
        
with open('tswift.csv', 'w', newline='') as file:
     writer = csv.writer(file)
     keys = list(song_individual[0].keys())
     header = [keys[x] for x in range(len(keys))]
     print(header)
     writer.writerow(header)
     lines = []
     for x in range (len(song_individual)):
         line = []
         for k in keys:
            line.append(song_individual[x][k])
         writer.writerow(line)
             
         

       
         
        
     
      
   

