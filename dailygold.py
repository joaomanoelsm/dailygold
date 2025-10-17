from flask import Flask, jsonify, request

app = Flask(__name__)

code = "PALZRVN1R8LMBDFGQ"

@app.route("/users", methods=["GET"])
def getCode():
    return jsonify(code)

print(code)

app.run(port=5000, host="https://dailygold.onrender.com", debug=True)