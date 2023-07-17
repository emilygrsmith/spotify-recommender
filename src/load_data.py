import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv
import os
from dotenv import load_dotenv
import time
import json
import requests
import pickle


load_dotenv()

PUBLIC_KEY = os.getenv('CLIENT_PUBLIC_KEY')
SECRET_KEY = os.getenv('CLIENT_SECRET_KEY')
client_credentials_manager = SpotifyClientCredentials(client_id=PUBLIC_KEY, client_secret=SECRET_KEY)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))


class Playlist:
    def __init__(self, id):
        self._playlistID = id
        self._length = 0
        self._playlistInfo = []
        self._token = self._acquire_token()
        self._info = self._loadPlayListInfo()
        
    def _loadPlayListInfo(self):
        info = sp.playlist_items(self._playlistID)
        self._length = len(info['items'])
        return info
    def getRecomend(self,filters = None):
        uris = []
        endpoint_url = "https://api.spotify.com/v1/recommendations?"
        
        for x in range(self._length):
            query = f"{endpoint_url}limit={1}&market=US&seed_tracks={self._info['items'][x]['track']['id']}"
            response =requests.get(query, 
                headers={"Content-Type":"application/json", 
                            "Authorization":f"Bearer {self._token}"})
            
            json_response = response.json()
            
            for i in json_response['tracks']:
                        uris.append(i)
        print(len(uris))            
        return uris


    def _acquire_token(self):
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
                response = requests.post(url, data=body_params, auth=(PUBLIC_KEY, SECRET_KEY))
                token_raw = json.loads(response.text)
                token = token_raw["access_token"]
                with open(token_cache_file, "wb") as fid:
                    pickle.dump(token, fid)
                return token
        else:
            grant_type = 'client_credentials'
            body_params = {'grant_type' : grant_type}
            url = 'https://accounts.spotify.com/api/token'
            response = requests.post(url, data=body_params, auth=(PUBLIC_KEY, SECRET_KEY))
            token_raw = json.loads(response.text)
            token = token_raw["access_token"]
            with open(token_cache_file, "wb") as fid:
                pickle.dump(token, fid)
            return token
if __name__ == "__main__":
    p = Playlist('3KkQ3MvqPUtnXSZQq08SOv')
    li = p.getRecomend()
    print (li)

    









# metrics for what this playlist says
 # popularity: are you underground or is this their most popular song?
 #explicit: ooo rebel
 # number o tracks: are u psycho normal or insane
 #generate a new playlis based on ur tendencies