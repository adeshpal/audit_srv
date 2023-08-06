import threading
import time
import logging as log
import pika

import src.AuditServices.EventSrv as EventSrv
import src.params as param

INITIAL_SLEEP_TIME = 30

class ConsumeAuditEvent(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.setName(name)
        log.warning("Thread started : %s", name)

    def run(self):
        time.sleep(INITIAL_SLEEP_TIME)
        self.consume_event()


    def consume_event(self):
        """ consume event from the queue and process into db"""
        log.warning("Event consumer started... : %s", "")

        connection_params = pika.ConnectionParameters(host=param.QUEUE_HOST,port=param.QUEUE_PORT)
        connection = pika.BlockingConnection(connection_params)
        channel = connection.channel()

        def on_message_received(ch, method, properties, body):
            log.warning("Consumer :: received new message : %s", body)
            EventSrv.create_event(body)

        channel.queue_declare(queue=param.QUEUE_NAME)
        channel.basic_consume(queue=param.QUEUE_NAME, auto_ack=True, 
                            on_message_callback=on_message_received)
        log.warning("starting consuming--->")
        channel.start_consuming()
