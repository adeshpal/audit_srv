"""
Database event operation layer
"""
import logging as log
import falcon
from src.schema.Admin import Admin
from  src.common import Utils as util

class DLAdmin:
    """DB operations on event_info table"""
    def create_admin(self, admin_details):
        """add event into db"""
        try:
            password = util.encoded_str(admin_details['email'])
            event_info = Admin(
                name=admin_details['name'],
                role= admin_details['role'],
                email=admin_details['email'],
                password=password,
            )
            return event_info.get_dict()
        except Exception as fault:
            log.error("Faild to add data into db, error=%s", fault)
            raise falcon.HTTPBadRequest(title="Invalid data", description="Try again with valid data!")

    def get_admin_details(self, email):
        """Get records by user"""
        log.warning("Getting admin info for user=%s", email)
        return Admin.select(Admin.q.email==email)
       
    def get_all_admins(self):
        """Get all records available in db"""
        log.warning("%s", "----Fetching all records-----")
        return Admin.select(orderBy=Admin.q.id)
