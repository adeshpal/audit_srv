"""
Version Handler
"""
import falcon

class ValidateParameter:
    """Validate parametes"""
    def validate_version(req, resp, resource, params, ALLOWED_VERSIONS):
        """"Suported versions"""
        if params.get('version') not in ALLOWED_VERSIONS:
            raise falcon.HTTPBadRequest(title='Wrong API Version',
            description="Please Provide valid API version to access resources")