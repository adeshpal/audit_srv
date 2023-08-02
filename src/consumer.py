import pika
import logging
import json
from src.DataLayer.DLEventInfo import process_event_into_db



def consume_event():
    logging.warning("-------in consume event is : %s", "")

    connection_params = pika.ConnectionParameters(host='172.17.0.2',port=5672)
    #connection_params = pika.ConnectionParameters(host='127.0.0.1',port=5672)

    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()

    def on_message_received(ch, method, properties, body):
        data = json.loads(body)
        logging.warning("received new message : %s", data)
        process_event_into_db(data)

    channel.queue_declare(queue='letterbox')
    channel.basic_consume(queue='letterbox', auto_ack=True, on_message_callback=on_message_received)
    logging.warning("starting consuming--->")
    channel.start_consuming()

# consume_event()
