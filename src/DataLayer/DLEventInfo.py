"""
Database event operation layer
"""
import logging as log
import falcon
from src.schema.EventInfo import EventInfo
class DLEventInfo:
    """DB operations on event_info table"""
    def create_event(self, event_details):
        """add event into db"""
        try:
            event_info = EventInfo(
                service_name=event_details['service_name'],
                user_id= event_details['user_id'],
                event_type=event_details['event_type'],
                service_id=event_details['service_id'],
                event_details=event_details['event_details']
            )
            return event_info.get_dict()
        except Exception as fault:
            log.error("Faild to add data into db, error=%s", fault)
            raise falcon.HTTPBadRequest(title="Invalid data", description="Try again with valid data!")
        

    def get_all_events(self):
        log.warning("%s", "----->> fetching all records")
        
        return EventInfo.select(orderBy=EventInfo.q.id)