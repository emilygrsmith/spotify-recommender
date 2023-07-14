import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv
import os
from dotenv import load_dotenv

load_dotenv()



#Authentication - without user
client_credentials_manager = SpotifyClientCredentials(client_id=os.getenv('CLIENT_PUBLIC_KEY'), client_secret=os.getenv('CLIENT_SECRET_KEY'))
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)


album = '1fnJ7k0bllNfL1kVdNVW1A'
results = sp.album_tracks(album)
print(len(results))
input()
artist = '06HL4z0CvFAxyc27GXpf02'
results = sp.artist_albums(artist)
album_ids = [results['items'][x]['id'] for x in range(len(results['items']))]

song_list = []
song_params = 0
for x in album_ids:
    song = sp.album_tracks(x, limit = 50)
    print(song['items'][0]['name'])
    input()
    song_params = len(song)
    print(song_params)
    song_list.append(song)
print(len(song_list[1]))
input()
with open('tswift.csv', 'w', newline='') as file:
     writer = csv.writer(file)
     keys = list(song_list[0]['items'][0].keys())
     header = [keys[x] for x in range(len(keys))]
     writer.writerow(header)
     for x in range (len(song_list)):
         print(song_list[x]['items'][0])
         lines=[]
         for y in range(len(song_list[x])):
             lineList = []
             for a in keys:
                 line = song_list[x]['items'][y][a]
                 lineList.append(line)
             lines.append(lineList)
    
         writer.writerows(lines)
         
        
     
      
   

