from dataclasses import dataclass
from netex.subscription_response_structure import SubscriptionResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class SubscriptionResponse(SubscriptionResponseStructure):
    """Response from Producer to Consumer to inform whether subscriptions have been
    created.

    Answers a previous SubscriptionRequest.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
