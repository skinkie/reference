from dataclasses import dataclass, field
from typing import List, Optional
from netex.type_of_infolink_enumeration import TypeOfInfolinkEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class InfoLinkStructure:
    """
    Type for Info LinK.

    :ivar value:
    :ivar type_of_info_link: Functional classifcation of infolink
    :ivar target_platform: Software platform for which link is targeted,
        eg ios, android
    """
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    type_of_info_link: List[TypeOfInfolinkEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "typeOfInfoLink",
            "type": "Attribute",
            "tokens": True,
        }
    )
    target_platform: Optional[object] = field(
        default=None,
        metadata={
            "name": "targetPlatform",
            "type": "Attribute",
        }
    )
