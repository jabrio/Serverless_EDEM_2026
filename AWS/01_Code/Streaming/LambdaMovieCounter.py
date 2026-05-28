""" 
Script: AWS Lambda. Perform Movie Count from Kinesis Data Streams.

Description: Lambda function that listens to events from Kinesis Data Streams
 and counts the occurrences of each movie in the stream.

EDEM. Master Big Data & Cloud 2025/2026
Professor: Javi Briones
"""

from collections import Counter
import logging
import base64
import json

# Set Logs
logging.getLogger().setLevel(logging.INFO)

""" Code: Entry point """
def lambda_handler(event, context):

    """
    Reads events from Kinesis Data Streams and counts the occurrences of each movie.

    Parameters:
        event (dict): The event payload that triggered the Lambda function.
            In this case, it contains records from Kinesis Data Streams.
        context (LambdaContext): Contains metadata about the invocation, function, and execution environment.

    Returns:
        dict: A response object with HTTP statusCode and body indicating the result.
    """

    movie_counter = Counter()

    for record in event["Records"]:

        # Decode Kinesis Message
        try:
            payload = json.loads(
                base64.b64decode(record["kinesis"]["data"])
            )

            movie_id = payload["item_id"]

            movie_counter[movie_id] += 1

        except Exception as e:
            logging.error(f"Error decoding Kinesis message: {e}")
            continue   

    logging.info(f"Movie counts: {dict(movie_counter)}")