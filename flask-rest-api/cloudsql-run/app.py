from flask import Flask, jsonify, request
import os

from cloud_sql import getSpeciesData

app = Flask(__name__)

@app.route("/species", methods=['GET'])
def get_species_info():
    args = request.args
    if len(args) != 1:
        return jsonify({'data':'invalid input'})
    #access cloud sql and fetch species information#
    result = getSpeciesData(args['name'])
    return jsonify({'data' : result})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
