from google.cloud import pubsub_v1
from edem_api.config import settings
import json

publisher = pubsub_v1.PublisherClient()

def publish_message(topic_id: str, message: dict):
    
    topic_path = publisher.topic_path(settings.PROJECT_ID, topic_id)
    future = publisher.publish(topic_path, json.dumps(message).encode("utf-8"))
    
    return future.result()