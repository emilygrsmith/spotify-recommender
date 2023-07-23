#!/bin/bash
source .env
source $PATH_TO_ENV


flask_cmd="cd src/app/ && flask run"
react_cmd="cd src/web-ui/ && npm start"


concurrently "$flask_cmd" "$react_cmd"