from dataclasses import dataclass, field
from typing import List, Optional

from .abstract_discovery_delivery_structure import AbstractDiscoveryDeliveryStructure
from .annotated_line_ref import AnnotatedLineRef
from .extensions_1 import Extensions1

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class LinesDeliveryStructure(AbstractDiscoveryDeliveryStructure):
    annotated_line_ref: List[AnnotatedLineRef] = field(
        default_factory=list,
        metadata={
            "name": "AnnotatedLineRef",
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
