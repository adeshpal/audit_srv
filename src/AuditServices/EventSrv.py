"""
Audit event service business logic
"""
import json
import logging as log
import falcon
import src.params as param
from src.DataLayer.DLEventInfo import DLEventInfo
from src.DataLayer.DLAdmin import DLAdmin
from src.DataLayer.DLUser import DLUser
from src.DataLayer.DLRole import DLRole

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
    response = {
        "status"  : param.SUCCESS, 
        "message" : "success", 
        "result"  : {}
        }
    try:
        #check user permission
        log.warning("Getting permission for user: %s", user_id)
        user = DLUser().get_user(user_id)
        if not user:
            response["message"] = "User not found!"
            resp.media = response
            return
        permissions = get_user_permissions(user.email)
        events = []
        if permissions == "all":
            events = DLEventInfo().get_all_events()
        else:
            events = DLEventInfo().get_user_events(user_id)
        # elif permissions:
        #     permission_arr = permissions.split(',')
        #     DLEventInfo().get_events_by_servie()
        result = [event.get_dict() for event in events]
        if len(result) == 0:
            response["message"] = "No matched record found!"
        response["result"] = result
        resp.status = falcon.HTTP_200
    except Exception as err:
        resp.status = falcon.HTTP_500
        response["message"] = "Failed to fetch data from DB."
        response["status"] = param.FAILED
        log.error("Failed to fetch data for=:%s, error:%s", user_id, err)
    
    resp.media = response

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


def get_user_permissions(email):
    """Method to get all use permissions"""
    try:
        admin_info = DLAdmin().get_admin_details(email)
        if admin_info:
            log.warning("Got Admin_info: %s, user=%s", str(admin_info[0]), err)
            role = DLRole().get_role_by_id(admin_info[0].role)
            log.warning("Role info for user=%s, role=%s",email, str(role))
            permissions = role.permissions
            log.warning("-------- permissions: %s", str(permissions))
            return permissions
    except Exception as err:
        log.warning("Unable to get permissions for user=:%s, error:%s", email, err)
    return ""
