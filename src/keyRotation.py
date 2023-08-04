from collections.abc import Callable, Iterable, Mapping
import threading
import src.AuditServices.EventSrv  as eventSrv
from src.DataLayer.DLEventInfo import DLEventInfo
import logging as log


class keyAuditKeyRotate(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.setName(name)
        log.warning("thread 2 name: %s", self.name)

    def run(self):
        result =  DLEventInfo().get_all_events()
        log.warning("-------->>> all result from key rotation: %s", str(result))
