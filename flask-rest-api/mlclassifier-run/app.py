from flask import Flask, jsonify, json, request
from google.cloud import pubsub_v1
from PIL import Image
import base64,io,os

from classifier import classify

app = Flask(__name__)

def publish_msg(userid, animal):
    publisher = pubsub_v1.PublisherClient()
    project_id = "glossy-chimera-350206"
    topic_id = "eyeam-loguser-topic"
    topic_path = publisher.topic_path(project_id, topic_id)

    data_str = '{"userid":"%s", "animal":"%s"}' % (userid, animal)
    data = data_str.encode("utf-8")
    future = publisher.publish(topic_path, data)

    return True

# url safe solution to decode base64 to fix padding issues
def decode_base64(data):
    data += '=' * (len(data) % 4)
    return base64.urlsafe_b64decode(data)

@app.route("/classifier", methods=['POST'])
def get_classification():
    img_b64 = request.form.get('user_image')
    img = base64.b64decode(img_b64)
    img = Image.open(io.BytesIO(img))
    result = str(classify(img))
    
    header = request.headers.get('X-Apigateway-Api-Userinfo')
    header = decode_base64(header)
    header = json.loads(header)

    userid = header['user_id']

    publish_msg(userid, result)
    
    return jsonify({'animalName' : result})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
'{"userid": "ffxiv",  "animal": "koala"}'