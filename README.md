#SETUP

```make sure to change all the host ip starting with 10.10.71.11 with your localhost IP```

$git clone https://github.com/aman5121993/grofKV.git/

$docker run -tdi --name redis -p 6379:6379 redis

$cd server

$docker build -t flaskserver ./

$docker run -tdi --name flaskserver -p 5000:5000 flaskserver


$cd websock

$docker build -t websocket ./

docker run -tdi --name websock -p 8765:8765 websock


$cd client

$docker build -t client ./

$docker run -ti client sh

```Entering the client shell```

$python client.py post animal --value tiger

$python client.py get animal

$python client.py watch animal
