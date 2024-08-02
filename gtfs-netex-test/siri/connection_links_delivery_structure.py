from dataclasses import dataclass, field
from typing import List, Optional

from .abstract_discovery_delivery_structure import AbstractDiscoveryDeliveryStructure
from .annotated_connection_link_ref import AnnotatedConnectionLinkRef
from .extensions_1 import Extensions1

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ConnectionLinksDeliveryStructure(AbstractDiscoveryDeliveryStructure):
    annotated_connection_link_ref: List[AnnotatedConnectionLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "AnnotatedConnectionLinkRef",
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
        init=False,
        default="2.1",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
