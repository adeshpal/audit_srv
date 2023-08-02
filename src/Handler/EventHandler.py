#Handler file to route all the incoming request to service
import falcon
from src.producer import produce_event
from src.consumer import consume_event
import logging
import json

API_VERSIONS = ['v1']
#ValidateParams
class ValidateParameter:
    def validate_version(self, req, resp, resource, params, API_VERSIONS):
        if params.get('version') not in API_VERSIONS:
            raise falcon.HTTPBadRequest(title='Invalid API Version',
            description="Please Provide valid API version to access resources")

# @falcon.before(ValidateParameter.validate_version, ['v1', 'v2'])
class EventHandler:
    def on_get(self, req, resp, version):
        logging.warning("--------->>> request in get eventHandler: req= %s, resp= %s, -- version=:%s", req, resp, version)
        consume_event()

    def on_post(self, req, resp, version):
        body = json.loads(req.stream.read())
        logging.warning("--------->>> request in eventHandler: req= %s, resp= %s, -- version=:%s and data= %s",
                        req, resp, version, body)
        # produce_event(body)
