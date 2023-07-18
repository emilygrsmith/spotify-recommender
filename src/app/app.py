from flask import Flask, request
import load_data as LD
import requests
app = Flask(__name__)
#app.register_blueprint()

@app.route('/data', methods = ['GET'])
def find_reccomended():
 
  try:
    id = request.args.get('id')
    playlist = LD.Playlist(id)
    uris = playlist.getRecomend()
  except Exception as e:
      print(e)
  
  return uris