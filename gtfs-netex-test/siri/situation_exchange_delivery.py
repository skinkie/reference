from dataclasses import dataclass

from .situation_exchange_delivery_structure import SituationExchangeDeliveryStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class SituationExchangeDelivery(SituationExchangeDeliveryStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
