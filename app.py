from flask import Flask,request,jsonify,json

app = Flask(__name__)

@app.route("/hello", methods=['GET'])
def hello():
    return "hello world!"
    

if __name__ == "__main__":
    app.run()
