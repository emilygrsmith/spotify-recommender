import spotipy

import csv
import os
from dotenv import load_dotenv
import time
import json
import requests
import pickle
import auth
load_dotenv()




class Playlist:
    def __init__(self, id,auth):
        print("INIT NEW")
        self._playlistID = id
        self._length = 0
        self._name = ""
        self._playlistInfo = []
        self._PUBLIC_KEY = os.getenv('CLIENT_PUBLIC_KEY')
        self._SECRET_KEY = os.getenv('CLIENT_SECRET_KEY')
        self._redirect = 'http://localhost:5000/callback' #CHANGE TO ENV
        self._ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
        #self._client_credentials_manager = SpotifyClientCredentials(client_id=self._PUBLIC_KEY, client_secret=self._SECRET_KEY)
        
        self.auth = auth
        
       # self._sp = spotipy.Spotify(client_credentials_manager = self._client_credentials_manager,scope="user-read-private user-read-email",redirect_uri = self._redirect)
        
        self._token = self.auth.authorize() if self.auth.get_auth_token() is  None else self.auth.get_auth_token()
        self._sp = spotipy.Spotify(self._token)
        self._info = self._loadPlayListInfo()
        self._uri = []

       
        
    def _loadPlayListInfo(self):
        info = self._sp.playlist_items(self._playlistID)
        self._name = self._sp.playlist(self._playlistID)['name']
        self._length = len(info['items'])
        return info
    def _sendRequest(self, request):
            response =requests.get(request, 
                headers={"Content-Type":"application/json", "scope":'user-read-private user-read-email',
                            "Authorization":f"Bearer {self._token}"})
            return response.json()

    def getRecomend(self,filters = None):
        uris = []
        endpoint_url = "https://api.spotify.com/v1/recommendations?"
        for x in range(self._length):
            
            query = f"{endpoint_url}limit={1}&market=US&seed_tracks={self._info['items'][x]['track']['id']}"
            json_response = self._sendRequest(query)
            print("GOT DA JSON")
            #print((json_response))
            for i in json_response['tracks']:
                name = i['name']
                new_request = i
                print(i['name'])
                while(name in uris):
                    print("REMOVING")
                    new_request = self._sendRequest(query)
                    #print(new_request.keys(),"IS NEW")
                    name = new_request['tracks'][0]['name']
                    new_request = new_request['tracks'][0]
                
                    
                self._uri.append(new_request)
                uris.append(name)
        #print(len(uris))
        self.buildPlaylist()           
        return uris
    def getUserID(self):
        user_info = self._sp.current_user()
        #print(user_info)
        return user_info
    def buildPlaylist(self):
        userInfo = self.getUserID()
        name = self._name + ": AI Version"
        newPlaylist = self._sp.user_playlist_create(userInfo['id'], name, public=True, collaborative=False, description='generaetd using AI model')
        newID = newPlaylist['id']
        for x in self._uri:
            toAdd = [x['uri']]
            self._sp.playlist_add_items(newID, toAdd)
    def _acquire_token(self):
        print("ACQUIRING TOKEN")
        token_cache_dir = os.path.join( self._ROOT_PATH, "cache")
        token_cache_file = os.path.join(token_cache_dir, "token.p")
        if os.path.exists(token_cache_file):
            current_time = time.time()
            if current_time - os.path.getmtime(token_cache_file) < 3600:
                with open(token_cache_file, "rb") as fid:
                    token = pickle.load(fid)
                    print("t")
                return token
            else:
                grant_type = 'client_credentials'
                body_params = {'grant_type' : grant_type, 'scope': 'user-read-private user-read-email'}
                url = 'https://accounts.spotify.com/api/token'
                response = requests.post(url, data=body_params, auth=(self._PUBLIC_KEY, self._SECRET_KEY))
                token_raw = json.loads(response.text)
                token = token_raw["access_token"]
                with open(token_cache_file, "wb") as fid:
                    pickle.dump(token, fid)
                    print("lol",token)
                return token
        else:
            grant_type = 'client_credentials'
            body_params = {'grant_type' : grant_type, 'scope': 'user-read-private user-read-email'}
            url = 'https://accounts.spotify.com/api/token'
            response = requests.post(url, data=body_params, auth=(self._PUBLIC_KEY, self._SECRET_KEY))
            token_raw = json.loads(response.text)
            token = token_raw["access_token"]
            with open(token_cache_file, "wb") as fid:
                pickle.dump(token, fid)
                print("TOKEN: ",token)
            return token
if __name__ == "__main__":
    p = Playlist('1prMoKRqh0BkGfSaniWkaC')
    #li = p.getRecomend()
    p.getRecomend()
    

    









# metrics for what this playlist says
 # popularity: are you underground or is this their most popular song?
 #explicit: ooo rebel
 # number o tracks: are u psycho normal or insane
 #generate a new playlis based on ur tendencies