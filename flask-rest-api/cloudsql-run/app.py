from flask import Flask, jsonify, json, request
import os

from cloud_sql import getSpeciesData, getUserLogs, decode_base64

app = Flask(__name__)

@app.route("/animal", methods=['GET'])
def get_animal_info(name):
    args = request.args
    args = args.to_dict()
    result = getSpeciesData(args.get('name'))
    return jsonify({'data' : result})

@app.route("/logs", methods=['GET'])
def get_user_log():
    header = request.headers.get('X-Apigateway-Api-Userinfo')
    header = decode_base64(header)
    header = json.loads(header)
    result = getUserLogs(header['user_id'])

    return jsonify({'data' : result})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
