from dataclasses import dataclass

from .situation_exchange_subscription_structure import SituationExchangeSubscriptionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class SituationExchangeSubscriptionRequest(SituationExchangeSubscriptionStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
