from dataclasses import dataclass
from netex.terminate_subscription_response_structure import TerminateSubscriptionResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class TerminateSubscriptionResponse(TerminateSubscriptionResponseStructure):
    """Request from Subscriber to Subscription Manager to terminate a subscription.

    Answered with a TerminateSubscriptionResponse.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
