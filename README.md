#SETUP

The setup consists of 3 containers/services. <br/>
1. Redis server which is used as the key-value store <br/>
2. Flask server that exposes the redis get and set methods <br/>
3. Client, that is a simple cli tool to get , post and watch key changed <br/>

At client side to watch the changes, PUB/SUB feature for redis is used that subscribe to all the key space notification. The method listen() is used to get the messages even if it is the blocking call because the script was doing nothing apart from priting the messages.


$git clone https://github.com/aman5121993/grofKV.git/ <br/>


$cd grofKV <br/>
$docker-compose up -d
$docker exec -ti redis redis-cli config set notify-keyspace-events KEA


```Redis is being used at the backend for the KeyValule Store``` <br/>

```Flask server is used for exposing the Get and Post Api``` <br/>

```Argparser client implemented to give options and listen to changes ``` <br/>
$docker exec -ti client sh <br/>
```Entering the client shell``` <br/>
$python client.py post --key animal --value tiger <br/>
$python client.py get --key animal <br/>
$python client.py watch <br/>

