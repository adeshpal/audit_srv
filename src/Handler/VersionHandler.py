"""
Version Handler
"""
import falcon

class ValidateParameter:
    """Validate parametes"""
    def validate_version(req, resp, resource, params, ALLOWED_VERSIONS):
        """"Suported versions"""
        if params.get('version') not in ALLOWED_VERSIONS:
            raise falcon.HTTPBadRequest(title='Unsupported API Version',
            description="Request API version is not found, retry with valid API version to access resources")