import argparse
import redis
import requests

def menu():
 parser = argparse.ArgumentParser()
 parser.add_argument("mode",help="enter mode get ,post or watch")
 parser.add_argument("--key",help="enter key")
 parser.add_argument("--value",help="Enter Value")
 args=parser.parse_args()
 
 if args.mode == "get":
  getmeth(args.key)
 if args.mode == "post":
  postmeth(args.key,args.value)
 if args.mode == "watch":
  watch() 

def getmeth(key):
 res=requests.get('http://10.10.71.11:5000/getkey/'+key)
 if res.ok:
  print (res.json())


def postmeth(key,val):
 payload = {"key": key,"value":val}
 r = requests.post('http://10.10.71.11:5000/postkey',json=payload)
 print (r.json())


def watch():
 r = redis.StrictRedis(host='10.10.71.11', port=6379)
 p = r.pubsub()
 p.psubscribe('__keyspace@0__:*')

 for message in p.listen():
  print ("Change in key: " + message['channel'].decode().split(':',1)[1])
 

if __name__ == "__main__":
 menu()
