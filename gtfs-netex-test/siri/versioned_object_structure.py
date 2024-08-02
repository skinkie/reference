from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from .modification_enumeration import ModificationEnumeration
from .status_enumeration import StatusEnumeration

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass(kw_only=True)
class VersionedObjectStructure:
    created: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    last_updated: XmlDateTime = field(
        metadata={
            "name": "lastUpdated",
            "type": "Attribute",
            "required": True,
        }
    )
    modification: ModificationEnumeration = field(
        default=ModificationEnumeration.NEW,
        metadata={
            "type": "Attribute",
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    status: StatusEnumeration = field(
        default=StatusEnumeration.ACTIVE,
        metadata={
            "type": "Attribute",
        },
    )
