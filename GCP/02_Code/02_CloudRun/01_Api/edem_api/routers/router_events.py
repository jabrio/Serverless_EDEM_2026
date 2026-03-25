from fastapi import APIRouter
from edem_api.repositories import repository_events

router = APIRouter(
    prefix="/events", tags=["edem_publish_messages"], responses={404: {"description": "Not found"}}
)

@router.post(
    path="/publish_events",
    summary="Publish messages to a Pub/Sub topic."
)

def publish_messages_to_pubsub(topic_id: str, message: dict):
    """
    Publish messages to a Pub/Sub topic.

    Args:
        topic_id (str): The ID of the Pub/Sub topic to which the messages will be published.
        message (str): The message to be published, in JSON format.
    Returns:
        A success message indicating that the messages were published successfully.
    """
    
    repository_events.publish_message(topic_id, message)
    return {"message": "Messages published successfully."}