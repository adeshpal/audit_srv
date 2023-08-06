"""
Database event operation layer
"""
import logging as log
import falcon
from src.schema.EventInfo import EventInfo
from src.schema.Role import Role
import sqlobject


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

    def get_user_events(self, user_id):
        """Get records by user"""
        log.warning("Fetching events of userID=%s", user_id)
        return EventInfo.select(EventInfo.q.user_id==int(user_id))
    
    def get_all_events(self):
        """Get all records available in db"""
        log.warning("%s", "----Fetching all records-----")
        return EventInfo.select(orderBy=EventInfo.q.id)

    def get_events_by_servie(self, services):
        """Get all records available in db"""
        try:
            log.warning("----Fetching records for services : %s", services)
            return EventInfo.select(sqlobject.IN(EventInfo.q.service_name, services))
        except sqlobject.SQLObjectNotFound as err:
            log.error("Faild to get data from db, error=%s", err)
        return []
    
    def get_events_before(self, end):
        """Get records available in db"""
        log.warning("----Fetching records till: %s", end)
        return EventInfo.select().filter(EventInfo.q.created_on<=end)
    
    def delete_events_before(self, end):
        """Delete all records available in db"""
        log.warning("----deleting records till: %s", end)
        return EventInfo.deleteMany(EventInfo.q.created_on<=end)
