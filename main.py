import json
import slack
from flask import Flask, request


#init flask stuff
app = Flask(__name__)



@app.route('/', methods=["POST"])
def web():
    payload = request.get_json()
    print(payload)

    return payload['challenge']

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)