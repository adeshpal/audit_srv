import sqlobject
from src import conn

class Role(sqlobject.SQLObject):
    """Role info"""
    _connection = conn
    name = sqlobject.StringCol(notNone=True)
    permissions = sqlobject.StringCol(default="")
    description = sqlobject.StringCol(default="")

    def get_dict(self):
        """resp dict"""
        return {
            "id": self.id,
            "name": self.name,
            "permissions": self.permissions,
            "description": self.description 
        }
Role.createTable(ifNotExists=True)
