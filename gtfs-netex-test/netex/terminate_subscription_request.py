from dataclasses import dataclass
from .terminate_subscription_request_structure import (
    TerminateSubscriptionRequestStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TerminateSubscriptionRequest(TerminateSubscriptionRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
