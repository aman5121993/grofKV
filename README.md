#SETUP

```make sure to change all the host ip starting with 10.10.71.11 with your localhost IP``` <br/>


$git clone https://github.com/aman5121993/grofKV.git/ <br/>


```Redis is being used at the backend for the KeyValule Store``` <br/>
$docker run -tdi --name redis -p 6379:6379 redis <br/>
$docker exec -ti redis redis-cli config set notify-keyspace-events KEA

```Flas server is used for exposing the Get and Post Api``` <br/>
$cd server <br/>
$docker build -t flaskserver ./ <br/>
$docker run -tdi --name flaskserver -p 5000:5000 flaskserver <br/>


```Argparser client implemented to give options and listen to changes ``` <br/>
$cd client <br/>
$docker build -t client ./ <br/>
$docker run -ti client sh <br/>
```Entering the client shell``` <br/>
$python client.py post animal --value tiger <br/>
$python client.py get animal <br/>
$python client.py watch <br/>

