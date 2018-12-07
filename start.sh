#!/bin/bash

startEngine()
{
	echo "Startowanie Serwera"
	python3 engine/main.py &
}

function startApp
{
	echo "Startowanie Strony"
	export FLASK_APP="app/hello.py"
	flask run &
}

startCamera()
{
	echo "Startowanie Kamer"
}

startEngine
sleep 1
startApp
sleep 1
startCamera
