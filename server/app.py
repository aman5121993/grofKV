from flask import Flask,request,jsonify
import redis

app = Flask(__name__)

r= redis.Redis(host='10.10.71.11',
port=6379,
db=0)


@app.route("/postkey", methods=['GET','POST'])
def postkey():
   if request.method == 'POST':
    cnt=request.json
    r.set(cnt['key'],cnt['value'])
    return jsonify({"response":"OK"})

@app.route("/getkey/<key>",methods=['GET'])
def getkey(key):
 print(key)
 return jsonify({"val":r.get(key)})

if __name__ == "__main__":
 app.run(debug=True,host='0.0.0.0')
