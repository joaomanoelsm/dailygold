from flask import Flask, jsonify, request

app = Flask(__name__)

code = "1BTSPKGT8AXQRVG3S"

@app.route("/", methods=["GET"])
def getCode():
    return jsonify(code)

print(code)

app.run(port=3000, host="0.0.0.0", debug=False)