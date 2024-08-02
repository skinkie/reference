from dataclasses import dataclass, field
from typing import List, Optional

from .abstract_service_delivery_structure import AbstractServiceDeliveryStructure
from .extensions_1 import Extensions1
from .general_message import GeneralMessage
from .general_message_cancellation import GeneralMessageCancellation

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class GeneralMessageDeliveryStructure(AbstractServiceDeliveryStructure):
    general_message: List[GeneralMessage] = field(
        default_factory=list,
        metadata={
            "name": "GeneralMessage",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    general_message_cancellation: List[GeneralMessageCancellation] = field(
        default_factory=list,
        metadata={
            "name": "GeneralMessageCancellation",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    version: str = field(
        default="2.1",
        metadata={
            "type": "Attribute",
        },
    )
