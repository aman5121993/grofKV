#SETUP

$git clone https://github.com/aman5121993/grofKV.git/

$docker run -tdi --name redis -p 6379:6379 redis

$cd flaskserver
```make sure to change redis host with your server ip```
$docker build -t flaskserver ./
$docker run -tdi --name flaskserver -p 5000:5000 flaskserver

$cd websock
$docker build -t websocket ./
docker run -tdi --name websock websock

$cd client
$docker build -t client ./
$docker run -ti client sh
