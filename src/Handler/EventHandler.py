#Handler file to route all the incoming request to service
import logging as log
import falcon
import src.params as param
from src.Handler.VersionHandler import ValidateParameter
import src.AuditServices.EventSrv as EventSrv

@falcon.before(ValidateParameter.validate_version, param.API_VERSIONS)
class EventHandler:
    """All consumer HTTP methods"""
    def on_get(self, req, resp, version):
        """Get event"""
        log.warning("on_get::Request details, req= %s, resp= %s, version=:%s",
                        req, resp, version)
        EventSrv.get_all_events(req, resp)

    def on_get_user(self, req, resp, version, user_id):
        """Get event"""
        log.warning("Request details, req= %s, resp= %s, version=:%s",
                        req, resp, version)
        EventSrv.get_user_events(req, resp, user_id)
