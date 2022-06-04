from flask import Flask, jsonify, request
from PIL import Image
import base64,io,os

from classifier import classify

app = Flask(__name__)

@app.route("/classifier", methods=['POST'])
def get_classification():
    img_b64 = request.form.get('user_image')
    img = base64.b64decode(img_b64)
    img = Image.open(io.BytesIO(img))
    result = str(classify(img))
    return jsonify({'animalName' : result})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
