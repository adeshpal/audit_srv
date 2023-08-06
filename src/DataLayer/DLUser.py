"""
Database event operation layer
"""
import logging as log
import falcon
from src.schema.User import User
from src.schema.Role import Role
import sqlobject

class DLUser:
    """DB operations on user table"""
    def create_user(self, user_details):
        """add user into db"""
        try:
            user_info = User(
                name=user_details['name'],
                email= user_details['email'],
                info=user_details['info'],
            )
            return user_info.get_dict()
        except Exception as fault:
            log.error("Faild to add data into db, error=%s", fault)
            raise falcon.HTTPBadRequest(title="Invalid data", description="Try again with valid data!")
    
    def get_user(self, user_id):
        """Get records by user"""
        try:
            log.warning("Getting user info for ID=%s", user_id)
            return User.get(int(user_id))
        except sqlobject.SQLObjectNotFound as err:
            log.error("User not found with id= %s, error=%s", user_id, err)
        return ""