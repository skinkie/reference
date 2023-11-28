from dataclasses import dataclass
from netex.unknown_subscription_error_structure import UnknownSubscriptionErrorStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class UnknownSubscriptionError(UnknownSubscriptionErrorStructure):
    """Error: Subscription not found."""
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
