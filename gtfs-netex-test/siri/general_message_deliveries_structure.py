from dataclasses import dataclass, field
from typing import List

from .general_message_delivery import GeneralMessageDelivery

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class GeneralMessageDeliveriesStructure:
    general_message_delivery: List[GeneralMessageDelivery] = field(
        default_factory=list,
        metadata={
            "name": "GeneralMessageDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
