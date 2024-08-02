from dataclasses import dataclass, field
from typing import Optional

from .abstract_discovery_request_structure import AbstractDiscoveryRequestStructure
from .extensions_1 import Extensions1

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class InfoChannelDiscoveryRequestStructure(AbstractDiscoveryRequestStructure):
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
