#Handler file to route all the incoming request to service
import logging as log
import falcon
import json
import src.params as param
from src.Handler.VersionHandler import ValidateParameter
import src.AuditServices.UserSrv as  UserSrv

@falcon.before(ValidateParameter.validate_version, param.API_VERSIONS)
class UserHandler:
    def on_post_create(self,
                       req,
                       resp,
                       version):
        """Create user"""
        request = json.loads(req.stream.read())
        UserSrv.create_user(request)
        resp.status = falcon.HTTP_201
    
    def on_post_admin(self,
                       req,
                       resp,
                       version):
        """Create user"""
        request = json.loads(req.stream.read())
        UserSrv.create_admin(request)
        resp.status = falcon.HTTP_201

