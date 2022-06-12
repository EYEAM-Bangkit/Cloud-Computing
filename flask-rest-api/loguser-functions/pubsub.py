#testing code to publish pubsub msg for triggering the cloud function.
from google.cloud import pubsub_v1

def publish_msg():
    publisher = pubsub_v1.PublisherClient()

    project_id = "[project-id]"
    topic_id = "[topic-id]"

    topic_path = publisher.topic_path(project_id, topic_id)

    data_str = f'{"userid": "Stranger","animal": "Monkey"}'
    data = data_str.encode("utf-8")
    future = publisher.publish(topic_path, data)
    print('published')
    return True