from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DistanceMatrixElementRefByValueStructure:
    """Type for a reference to a LINK.

    by O/D value

    :ivar name_of_class: Name of class of LINK.
    :ivar created: Date reference was first created.
    :ivar changed: Date reference was last changed.
    :ivar version: Version number of referenced entity.
    :ivar from_ref: Identifier of a POINT. at which LINK starts.
    :ivar to_ref: Identifier of a POINT. at which LINK ends.
    :ivar name_of_point_ref_class: Class of POINT referenced by LINK.
    """
    name_of_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameOfClass",
            "type": "Attribute",
        }
    )
    created: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    changed: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    from_ref: str = field(
        metadata={
            "name": "fromRef",
            "type": "Attribute",
            "required": True,
        }
    )
    to_ref: str = field(
        metadata={
            "name": "toRef",
            "type": "Attribute",
            "required": True,
        }
    )
    name_of_point_ref_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameOfPointRefClass",
            "type": "Attribute",
        }
    )
