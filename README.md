# Spotify Recommender Web App

What is it: A web app using flask and React that implements the Spotify API to recommend and build a playlist based off of a user's chosen playlist. Using the Spotify API's recommendation functionality, the app reccomends an equal-length playlist and automatically places it in the user's library!

How to use it yourself:

Clone the repo and create a .env file that has this format:

CLIENT_SECRET_KEY=XXXXXXXXX
CLIENT_PUBLIC_KEY=XXXXXXXXXXXX
PYTHONUNBUFFERED=0
PATH_TO_ENV=../pathto/virtualenvironment

The API keys for Spotify can be accessed here: https://developer.spotify.com/
Create a Spotify developer account and place your public/private keys in the .env file

Create a python virtual environment wherever you prefer and place the path to the venv in the .env file as well. Install the modules found in requirements.txt to your virtual environment (pip/pip3 install -r requirements.txt)

Finally, run npm install in the src/web-app directory to complete the build of the project. 

In the main directory, run ./run.sh to launch the app!


The playlist link of any of your playlists can be found by copying the shareable link of any playlist on Spotify!

The playlist ID below would be 3wn372MvCPfmpOqEwMtBXQ for example

<img width="653" alt="Screen Shot 2023-07-23 at 3 03 44 PM" src="https://github.com/emilygrsmith/spotify-recommender/assets/91433035/2f9a2dff-718f-4f0d-b017-6f9979fef635">

