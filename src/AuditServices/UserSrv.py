"""
Action on ssers
"""
import json
import logging as log
from src.DataLayer.DLUser import DLUser
from src.DataLayer.DLAdmin import DLAdmin

def create_user(user_details):
    """Add event into database"""
    try:
        # data = json.loads(user_details)
        log.warning("Processing to create = %s", str(user_details))
        event_info = DLUser().create_user(user_details)
        log.warning("---- User created ----, data= %s", str(event_info))
    except Exception as err:
        log.error("Unable to add user into db, error=%s", err)

def create_admin(user_details):
    """Add event into database"""
    try:
        # data = json.loads(user_details)
        DLAdmin().create_admin(user_details)
        log.warning("---- Admin created ----, data= %s", str(user_details))
    except Exception as err:
        log.error("Unable to add admin into db, error=%s", err)