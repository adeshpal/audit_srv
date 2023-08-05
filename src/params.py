"""Parameters/Const used in service"""

#Supported api versions
API_VERSIONS = ['v1']

#Repsonse status
SUCCESS=1
FAILED=0

#Queue params
QUEUE_HOST='172.17.0.2'
QUEUE_PORT=5672
QUEUE_NAME='audit_queue'

#Services
USER_SERVICE="userSrv"
DEVICE_SERVICE="deviceSrv"
LICENSE_SERVICE="licenseSrv"


#Events
USER_CREATE = "userCreate"


# key rotation config values
