import sqlobject
from src import conn

class Role(sqlobject.SQLObject):
    """Role info"""
    _connection = conn
    name = sqlobject.IntCol(default=0)
    description = sqlobject.StringCol(length=30, notNone=True)
    permissions = sqlobject.StringCol(notNone=True)

    def get_dict(self):
        """resp dict"""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "permissions": self.permissions,
           
        }
Role.createTable(ifNotExists=True)
