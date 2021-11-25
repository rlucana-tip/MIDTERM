#!/bin/bash

docker build -t midtermapp .
docker run -t -d -p 5000:5000 --name midtermapprun midtermapp
docker ps -a