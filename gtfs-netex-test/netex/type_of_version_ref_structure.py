from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from .modification_enumeration import ModificationEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfVersionRefStructure:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    name_of_ref_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameOfRefClass",
            "type": "Attribute",
        },
    )
    created: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    changed: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    modification: Optional[ModificationEnumeration] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    ref: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    version_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "versionRef",
            "type": "Attribute",
        },
    )
