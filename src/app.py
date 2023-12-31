# import threading
from src.routes import get_app

application = get_app()

from src.consumer import ConsumeAuditEvent 
consumer_thread = ConsumeAuditEvent("Consume audit event thread")
consumer_thread.start()


from src.LogRetention import keyAuditKeyRotate
key_rotate = keyAuditKeyRotate("Key rotation thread")
key_rotate.start()

