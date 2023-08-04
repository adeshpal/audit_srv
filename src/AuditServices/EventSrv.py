"""
Audit event service business logic
"""
import json
import logging as log
import falcon
import src.params as param
from src.DataLayer.DLEventInfo import DLEventInfo


def create_event(event_details):
    """Add event into database"""
    try:
        data = json.loads(event_details)
        log.warning("Processing event into db = %s", str(data))
        event_info = DLEventInfo().create_event(data)
        log.warning("---- Event created ----, data= %s", str(event_info))
    except Exception as err:
        log.error("Unable to add event into db, error=%s", err)

def get_user_events(req, resp, user_id):
    """all events created by the specific user"""
    return

def get_service_events():
    """
    all events created by the specific 
    user who has access to other service as well
    """
    return

def get_all_events(req, resp):
    """view all events"""
    response = {
        "status"  : param.SUCCESS, 
        "message" : "success", 
        "result"  : {}
        }
    result = []
    try:
        events =  DLEventInfo().get_all_events()
        result = [event.get_dict() for event in events]
        response["result"] = result
        resp.media = response
    except Exception as err:
        resp.status = falcon.HTTP_500
        response["message"] = "Failed to fetch data"
        response["status"] = param.FAILED
        log.error("Data fetch failed, error:%s", err)
    resp.media = response
