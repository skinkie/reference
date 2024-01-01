from dataclasses import dataclass
from .heartbeat_notification_structure import HeartbeatNotificationStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class HeartbeatNotification(HeartbeatNotificationStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
