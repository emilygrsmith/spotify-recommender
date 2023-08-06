from flask import Flask, request
import load_data as LD
import requests
import auth 
app = Flask(__name__)

playlist = 1
auth = auth.Auth()
@app.route('/data', methods = ['GET'])
def find_reccomended():
  try:
    id = request.args.get('id')
    print(id)
    idList = id.split('/')
    print(idList)
    newID = idList[4]
    newID= newID[0:newID.index('?')]
    playlist = LD.Playlist(newID,auth)
    print("INSTANT")
    uris = playlist.getRecomend()
  except Exception as e:
      print(e)
  
  return uris

@app.route('/build', methods =['GET','POST'])
def build_playlist():
  print(playlist)

@app.route('/callback')
def callback():
    print("coding")
    code = request.args.get('code')
    auth.set_authorization_code(code)  # Store the code in the Auth instance
    return 'Code received. You can close this window now.'