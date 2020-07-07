from flask import Flask,request,jsonify,json

app = Flask(__name__)

@app.route("/hello", methods=['GET'])
def hello():
    return "hello beautiful world!"
    

if __name__ == "__main__":
    app.run("0.0.0.0")
