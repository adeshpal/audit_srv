#Handler file to route all the incoming request to service
import logging as log
import falcon
import src.params as param
from src.Handler.VersionHandler import ValidateParameter
from src.common import Utils as util

@falcon.before(ValidateParameter.validate_version, param.API_VERSIONS)
class AuthHandler:
    """All consumer HTTP methods"""
    def on_get(self, req, resp, version, user_id, service_name):
        """Get event"""
        log.warning("on_get::Request details, req= %s, resp= %s, version=:%s",
                        req, resp, version)
        payload = {"user_id" :user_id, "service_name": service_name}
        token = util.get_jwt_token(payload)
        if token :
            resp.media = {"jwt":token}
            resp.status = falcon.HTTP_201
        else:
            resp.status = falcon.HTTP_500
            resp.media = {"message":"Please check failure logs..."}
