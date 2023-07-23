#!/bin/bash

source ../spotify-env/bin/activate


flask_cmd="cd src/app/ && flask run"
react_cmd="cd src/web-ui/ && npm start"


concurrently "$flask_cmd" "$react_cmd"