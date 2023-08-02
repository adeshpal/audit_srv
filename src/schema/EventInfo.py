import sqlobject
from src import conn
from datetime import datetime

class EventInfo(sqlobject.SQLObject):
    """Event info table"""
    _connection = conn
    user_id = sqlobject.IntCol(default=0)
    event_type = sqlobject.StringCol(notNone=True)
    service_id = sqlobject.IntCol(default=0)  
    service_name = sqlobject.StringCol(notNone=True)
    event_details = sqlobject.JSONCol(default = {})
    created_on = sqlobject.DateTimeCol(default=datetime.now(), sqlType='DATETIME')

    def get_dict(self):
        """resp dict"""
        return {
            "id": self.id,
            "user_id": self.user_id,
            "event_type": self.event_type,
            "service_id": self.service_id,
            "service_name": self.service_name,
            "event_details": self.event_details,
            "created_on": self.created_on,
        }
EventInfo.createTable(ifNotExists=True)
