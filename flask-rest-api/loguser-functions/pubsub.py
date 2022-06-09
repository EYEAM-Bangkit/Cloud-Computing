#testing code for triggering the cloud function
from google.cloud import pubsub_v1

def publish_msg():
    publisher = pubsub_v1.PublisherClient()

    project_id = "glossy-chimera-350206"
    topic_id = "eyeam-loguser-topic"

    topic_path = publisher.topic_path(project_id, topic_id)

    data_str = f'{"userid": "Stranger","animal": "Monkey"}'
    data = data_str.encode("utf-8")
    future = publisher.publish(topic_path, data)

    return True