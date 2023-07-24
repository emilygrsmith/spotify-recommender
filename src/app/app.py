from flask import Flask, request
import load_data as LD
import requests

app = Flask(__name__)

playlist = 1
@app.route('/data', methods = ['GET'])
def find_reccomended():
 
  try:
    id = request.args.get('id')
    idList = id.split('/')
    newID = idList[4]
    newID= newID[0:newID.index('?')]
    playlist = LD.Playlist(newID)
    uris = playlist.getRecomend()
  except Exception as e:
      print(e)
  
  return uris

@app.route('/build', methods =['GET','POST'])
def build_playlist():
  print(playlist)