import argparse
import requests
import asyncio
import websockets

def menu():
 parser = argparse.ArgumentParser()
 parser.add_argument("mode",help="enter mode get ,post or watch")
 parser.add_argument("key",help="enter key")
 parser.add_argument("--value",help="Enter Value")
 args=parser.parse_args()
 
 if args.mode == "get":
  getmeth(args.key)
 if args.mode == "post":
  postmeth(args.key,args.value)
 if args.mode == "watch":
  print ("value is")
  getmeth(args.key)
  asyncio.get_event_loop().run_until_complete(hello(args.key))
 

def getmeth(key):
 res=requests.get('http://10.10.71.11:5000/getkey/'+key)
 if res.ok:
  print (res.json())


def postmeth(key,val):
 payload = {"key": key,"value":val}
 r = requests.post('http://10.10.71.11:5000/postkey',json=payload)
 print (r.json())


async def hello(key):
  val1=''
  while True:
    async with websockets.connect(
            'ws://10.10.71.11:8765') as websocket:

        await websocket.send(key)
        val = await websocket.recv()
        if val[2:-1] != val1:
         print("Value Now Is:" + val[2:-1])
         val1=val[2:-1]



if __name__ == "__main__":
 menu()
