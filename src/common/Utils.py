"""
Common lib methods for auditSrv
"""
import base64
import jwt
import logging as log

def encoded_str(key):
    """
    Get encoded base64 string
    """

    key_bytes = key.encode("ascii")
    base64_bytes = base64.b64encode(key_bytes)
    base64_string = base64_bytes.decode("ascii")
    print(f"Encoded string: {base64_string}")
    return base64_string


def decoded_str(key):
    """
    Get decoded base64 string
    """
    base64_bytes = key.encode("ascii")
    
    key_bytes = base64.b64decode(base64_bytes)
    str_key = key_bytes.decode("ascii")
    
    print(f"Decoded string: {str_key}")
    return str_key

def get_jwt_token(payload):
    try:
        encoded_jwt = jwt.encode(
            {
                "user_id" : payload["user_id"],
                "service_name" : payload["service_name"]
            },
            "secret", 
            algorithm="HS256")
        return encoded_jwt
    except Exception as err:
        log.error("Unable to generate jwt token, error:=%s", err)
    return None

"""
payload = {"user_id" :1}
token = jwt.encode({"user_id" :1}, "secret", algorithm="HS256")
"""