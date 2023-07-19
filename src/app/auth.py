
#NOT IMPORTANT RIGHT NOW BUT CAN BE USED LATER FOR OTHER USERS TO ACCCESS SITE

import random
import math
import hashlib
import base64
import os
import dotenv
import urllib.parse

load_dotenv()

class Auth:
    def __init__(self):
        self._code = None
        self._PUBLIC_KEY = os.getenv('CLIENT_PUBLIC_KEY')
        self._redirect = '500.0.0.0'
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
    def authorize(self):
        code_verifier = self.generateRandomString(128)
        code_challenge = self.generateCodeChallenge(code_verifier)
        state = self.generateRandomString(16)
        scope = 'user-read-private user-read-email'
        args = urllib.parse.urlencode({
    'response_type': response_type,
    'client_id': client_id,
    'scope': scope,
    'redirect_uri': redirect_uri,
    'state': state,
    'code_challenge_method': code_challenge_method,
    'code_challenge': code_challenge,
})

url = 'https://accounts.spotify.com/authorize?' + args

def main():
    a = Auth()
    x = a.generateRandomString(10)
    print(x)
main()
