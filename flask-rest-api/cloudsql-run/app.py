from flask import Flask, jsonify, request
import os

from cloud_sql import getSpeciesData, getUserLogs

app = Flask(__name__)

@app.route("/animal/<name>", methods=['GET'])
def get_species_info(name):
    result = getSpeciesData(name)
    return jsonify({'data' : result})

@app.route("/logs/<user_id>", methods=['GET'])
def get_species_info(user_id):
    result = getUserLogs(user_id)
    return jsonify({'data' : result})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
