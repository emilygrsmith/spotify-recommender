import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv
import os
from dotenv import load_dotenv

load_dotenv()



#Authentication - without user
client_credentials_manager = SpotifyClientCredentials(client_id=os.getenv('CLIENT_PUBLIC_KEY'), client_secret=os.getenv('CLIENT_SECRET_KEY'))
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)


# album = '1fnJ7k0bllNfL1kVdNVW1A'
# results = sp.album_tracks(album)

# results = sp.search(q='Taylor Swift', type='artist')
# artist_id = results['artists']['items'][0]['id']

# albums = sp.artist_albums(artist_id, album_type='album')

# red_album = None
# for album in albums['items']:
#     if album['name'] == 'Red':
#         red_album = album
#         break
# if red_album:
#     tracks = sp.album_tracks(red_album['id'])
    
#     for track in tracks['items']:
#         print(track['name'])
# input()





artist = '06HL4z0CvFAxyc27GXpf02'
results = sp.artist_albums(artist)
album_ids = [results['items'][x]['id'] for x in range(len(results['items']))]

song_list = []
song_params = 0
for x in album_ids:
    song = sp.album_tracks(x, limit = 50)
   
    song_params = len(song)
   
    song_list.append(song)


with open('tswift.csv', 'w', newline='') as file:
     writer = csv.writer(file)
     keys = list(song_list[0]['items'][0].keys())
     header = [keys[x] for x in range(len(keys))]
     print(header)
     writer.writerow(header)
     lines = []
     for x in range (len(song_list)):
         pass
             
         
    
       
         
        
     
      
   

