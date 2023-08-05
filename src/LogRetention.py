import logging as log
import datetime
import time
import threading
from src.DataLayer.DLEventInfo import DLEventInfo
from dateutil.relativedelta import relativedelta


LOG_RETENTION_TIME = 15 # Days
INITIAL_SLEEP = 60 # seconds

class keyAuditKeyRotate(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.setName(name)
        log.warning("thread 2 name: %s", self.name)

    def run(self):
        time.sleep(INITIAL_SLEEP)
        today = datetime.datetime.today()
        end = today - relativedelta(day=LOG_RETENTION_TIME)
        log.warning("---> Fetching event before: %s", end)
        result =  DLEventInfo().get_events_before(end)
        log.warning("-------->>> all result from key rotation: %s", str(result))
        
