from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {
        "id": 1,
        "name": "Satoru gozo",
        "age": 23
    },
    {
        "id": 2,
        "name": "Sucumba",
        "age": 120
    },
    {
        "id": 3,
        "name": "Itaduro",
        "age": 17
    },
]

@app.route("/users", methods=["GET"])
def getUser():
    return jsonify(users)

print(users[0]["age"])

app.run(port=5000, host="localhost", debug=True)