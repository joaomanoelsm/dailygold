from flask import Flask, jsonify, request

app = Flask(__name__)

codes = {
    "goldenCode": "D1XMLNVPKLCO7FSEU",
    "telegramCode": "",
    "xCode": "",
    "metaCode": "X7K9P",
    "discCode": "",
    "faceitCode": ""
}

@app.route("/", methods=["GET"])
def getCode():
    return jsonify(codes.goldenCode)

print(codes)

app.run(port=3000, host="0.0.0.0", debug=False)
