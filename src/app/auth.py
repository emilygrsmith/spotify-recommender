
#NOT IMPORTANT RIGHT NOW BUT CAN BE USED LATER FOR OTHER USERS TO ACCCESS SITE

import random
import math
import socketserver
import hashlib
import base64
import os
import time
from dotenv import load_dotenv
import urllib.parse
import requests
from urllib.parse import urlparse, parse_qs
import http.server
import random
import string
import threading
import webbrowser
import http.server
import flask
load_dotenv()
class Auth:
     
     def __init__(self):
        self._code = None
        self._PUBLIC_KEY = os.getenv('CLIENT_PUBLIC_KEY')
        self._redirect = 'http://localhost:5000/callback'
        self.authorization_code = None
        self._token = None
     def generateRandomString(self,length):
        text = ""
        possible = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        for x in range(length):
            text = text + possible[math.floor(random.uniform(0,1)*len(possible))]
        return text
    
     def generateCodeChallenge(self,codeVerifier):
        def base64encode(data):
            return base64.urlsafe_b64encode(data).rstrip(b'=').decode('utf-8')

        encoder = hashlib.sha256()
        encoder.update(codeVerifier.encode('utf-8'))
        digest = encoder.digest()

        return base64encode(digest)
     def set_authorization_code(self,code):
         self.authorization_code = code
     def get_auth_token(self):
        return self._token
     def authorize(self): 
        client_id =  self._PUBLIC_KEY
        redirect_uri = self._redirect
        scope = 'user-read-private user-read-email playlist-modify-private playlist-modify-public'

        code_verifier = self.generateRandomString(128)
        code_challenge = self.generateCodeChallenge(code_verifier)

        state = self.generateRandomString(16)

        authorization_base_url = 'https://accounts.spotify.com/authorize'
        authorization_params = {
    'response_type': 'code',
    'client_id': client_id,
    'scope': scope,
    'redirect_uri': redirect_uri,
    'state': state,
    'code_challenge_method': 'S256',
    'code_challenge': code_challenge
}

        authorization_url = authorization_base_url + '?' + urllib.parse.urlencode(authorization_params)
       

        webbrowser.open(authorization_url)
        
        max_wait_time = 8  # Maximum time to wait for the code (in seconds)
        wait_interval = 2   # Time interval between checks (in seconds)
        wait_time = 0

        while not self.authorization_code and wait_time < max_wait_time:
            time.sleep(wait_interval)
            wait_time += wait_interval
        
       
        print(self.authorization_code,"AUTH CODE")
        # Exchange the 'code' for an access token
        token_url = 'https://accounts.spotify.com/api/token'
        token_params = {
            'grant_type': 'authorization_code',
            'code': self.authorization_code,
            'redirect_uri': redirect_uri,
            'client_id': client_id,
            'code_verifier': code_verifier
        }

        response = requests.post(token_url, data=token_params)
        if response.ok:
            access_token = response.json()['access_token']
            print("Access Token:", access_token)
            self._token = access_token
            return access_token
        else:
            print("Failed to obtain Access Token:", response.json())
        



