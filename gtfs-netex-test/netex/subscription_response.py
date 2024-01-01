from dataclasses import dataclass
from .subscription_response_structure import SubscriptionResponseStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class SubscriptionResponse(SubscriptionResponseStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
