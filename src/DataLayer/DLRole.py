"""
Database event operation layer
"""
import logging as log
import falcon
from src.schema.User import User
from src.schema.Role import Role
class DLRole:
    """DB operations on role table"""
    def get_role_by_id(self, id):
        """Get records by user"""
        log.warning("----Fetching records for roleid=%s", id)
        return Role.get(int(id))