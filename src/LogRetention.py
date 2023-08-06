import logging as log
import datetime
import time
import threading
from src.DataLayer.DLEventInfo import DLEventInfo
from dateutil.relativedelta import relativedelta
import src.common.MessageWriter as MessageWriter
import os
LOG_RETENTION_TIME = 15 # Days
INITIAL_SLEEP = 10 # seconds

class keyAuditKeyRotate(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.setName(name)
        log.warning("thread 2 name: %s", self.name)

    def run(self):
        time.sleep(INITIAL_SLEEP)
        today = datetime.datetime.today()
        end = today - relativedelta(days=LOG_RETENTION_TIME)
        log.warning("---> Fetching event before: %s, from=%s", end, today)
        events =  DLEventInfo().get_events_before(end)
        file_name = "events-log-"+ end.strftime("%b-%d-%Y-%H-%M-%S")+".txt"
        MessageWriter.write_message(file_name, events)
        log.warning("Events clean up from db: %s", str(events))
        DLEventInfo().delete_events_before(end)
