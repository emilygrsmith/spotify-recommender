import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv
import os
from dotenv import load_dotenv
import time

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
def acquire_token():
    """Fetches a Spotify web API token"""
    token_cache_dir = os.path.join(ROOT_PATH, "cache")
    token_cache_file = os.path.join(token_cache_dir, "token.p")
    if os.path.exists(token_cache_file):
        current_time = time.time()
        if current_time - os.path.getmtime(token_cache_file) < 3600:
            with open(token_cache_file, "rb") as fid:
                token = pickle.load(fid)
            return token
        else:
            grant_type = 'client_credentials'
            body_params = {'grant_type' : grant_type}
            url = 'https://accounts.spotify.com/api/token'
            response = requests.post(url, data=body_params, auth=(CLIENT_ID, CLIENT_SECRET))
            token_raw = json.loads(response.text)
            token = token_raw["access_token"]
            with open(token_cache_file, "wb") as fid:
                pickle.dump(token, fid)
            return token
    else:
        grant_type = 'client_credentials'
        body_params = {'grant_type' : grant_type}
        url = 'https://accounts.spotify.com/api/token'
        response = requests.post(url, data=body_params, auth=(CLIENT_ID, CLIENT_SECRET))
        token_raw = json.loads(response.text)
        token = token_raw["access_token"]
        with open(token_cache_file, "wb") as fid:
            pickle.dump(token, fid)
        return token
if __name__ == "__main__":
    p = Playlist('3KkQ3MvqPUtnXSZQq08SOv')
    print(acquire_token())



# metrics for what this playlist says
 # popularity: are you underground or is this their most popular song?
 #explicit: ooo rebel
 # number o tracks: are u psycho normal or insane
 #generate a new playlis based on ur tendencies