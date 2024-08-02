from dataclasses import dataclass, field
from typing import Optional

from .abstract_subscription_structure import AbstractSubscriptionStructure
from .extensions_1 import Extensions1
from .general_message_request import GeneralMessageRequest

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class GeneralMessageSubscriptionStructure(AbstractSubscriptionStructure):
    general_message_request: GeneralMessageRequest = field(
        metadata={
            "name": "GeneralMessageRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
