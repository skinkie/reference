from dataclasses import dataclass

from .subscription_qualifier_structure import SubscriptionQualifierStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class SubscriptionRefStructure(SubscriptionQualifierStructure):
    pass
