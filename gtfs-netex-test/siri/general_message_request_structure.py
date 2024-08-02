from dataclasses import dataclass, field
from typing import List, Optional

from .abstract_functional_service_request_structure import AbstractFunctionalServiceRequestStructure
from .extensions_1 import Extensions1
from .info_channel_ref_structure import InfoChannelRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class GeneralMessageRequestStructure(AbstractFunctionalServiceRequestStructure):
    info_channel_ref: List[InfoChannelRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "InfoChannelRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    language: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Language",
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
