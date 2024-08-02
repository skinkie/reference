from dataclasses import dataclass, field
from typing import List

from .situation_exchange_delivery import SituationExchangeDelivery

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class SituationExchangeDeliveriesStructure:
    situation_exchange_delivery: List[SituationExchangeDelivery] = field(
        default_factory=list,
        metadata={
            "name": "SituationExchangeDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
