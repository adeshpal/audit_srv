
from src.schema import EventInfo as event
import logging


def process_event_into_db(event_details):
    logging.warning("****** entry to be added: %s", str(event_details))
    eventInfo = event.EventInfo(
        service_name=event_details['service_name'],
        user_id= event_details['user_id'],
        event_type=event_details['event_type'],
        service_id=event_details['service_id'],
        event_details=event_details['event_details']
        )
    logging.warning("****** entry created: %s", str(eventInfo))

    