import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv
import os
from dotenv import load_dotenv

load_dotenv()

client_credentials_manager = SpotifyClientCredentials(client_id=os.getenv('CLIENT_PUBLIC_KEY'), client_secret=os.getenv('CLIENT_SECRET_KEY'))
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

class Playlist:
    def __init__(self, id):
        self._playlistID = id
        self._playlistInfo = []

        self._loadPlayListInfo()

    def _loadPlayListInfo(self):
        results = sp.playlist_items(self._playlistID)
        print(results['items'][0]['track']['track'])
if __name__ == "__main__":
    p = Playlist('3KkQ3MvqPUtnXSZQq08SOv')



# metrics for what this playlist says
 # popularity: are you underground or is this their most popular song?
 #explicit: 