from dataclasses import dataclass
from .subscription_terminated_notification_structure import (
    SubscriptionTerminatedNotificationStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class SubscriptionTerminatedNotification(
    SubscriptionTerminatedNotificationStructure
):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
