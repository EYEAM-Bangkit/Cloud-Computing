from flask import Flask, jsonify, request
import os

#from app.classifier import classify
#from app.cloud_sql import sql

app = Flask(__name__)

@app.route("/classifier", methods=['POST'])
def get_classification():
    #classify image using the model#
    result = '#classification#'
    return jsonify({'data' : result})

@app.route("/species", methods=['GET'])
def get_species_info():
    args = request.args
    if len(args) != 1:
        return jsonify({'data':'invalid input'})
    #access cloud sql and fetch species information#
    result = '#species info'
    return jsonify({'data' : result})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 4000)))
