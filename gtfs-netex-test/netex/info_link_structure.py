from dataclasses import dataclass, field
from typing import Optional

from .type_of_info_link_enumeration import TypeOfInfoLinkEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class InfoLinkStructure:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    type_of_info_link: list[TypeOfInfoLinkEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "typeOfInfoLink",
            "type": "Attribute",
            "tokens": True,
        },
    )
    target_platform: Optional[object] = field(
        default=None,
        metadata={
            "name": "targetPlatform",
            "type": "Attribute",
        },
    )
