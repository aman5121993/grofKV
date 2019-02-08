#SETUP

```make sure to change all the host ip starting with 10.10.71.11 with your localhost IP``` <br/>


$git clone https://github.com/aman5121993/grofKV.git/ <br/>


```Redis is being used at the backend for the KeyValule Store``` <br/>
$docker run -tdi --name redis -p 6379:6379 redis <br/>

```Flas server is used for exposing the Get and Post Api``` <br/>
$cd server <br/>
$docker build -t flaskserver ./ <br/>
$docker run -tdi --name flaskserver -p 5000:5000 flaskserver <br/>


```Websocket server implement for the Async call and watching the changes``` <br/>
$cd websock <br/>
$docker build -t websocket ./ <br/>
docker run -tdi --name websock -p 8765:8765 websock <br/>


```Argparser and websocker server implemented to give options and listen to changes ``` <br/>
$cd client <br/>
$docker build -t client ./ <br/>
$docker run -ti client sh <br/>
```Entering the client shell``` <br/>
$python client.py post animal --value tiger <br/>
$python client.py get animal <br/>
$python client.py watch animal <br/>

![alt text](https://i.postimg.cc/jdMrWjqQ/grof1.png)
