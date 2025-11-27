from flask import Flask, jsonify, request

app = Flask(__name__)

code = "4MOBDXGLM6HI50KG5"

@app.route("/", methods=["GET"])
def getCode():
    return jsonify(code)

print(code)

app.run(port=3000, host="0.0.0.0", debug=False)