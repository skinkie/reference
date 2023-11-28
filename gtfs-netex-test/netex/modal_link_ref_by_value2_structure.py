from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from netex.all_modes_enumeration import AllModesEnumeration
from netex.point_ref_structure import PointRefStructure
from netex.type_of_link_ref import TypeOfLinkRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ModalLinkRefByValue2Structure:
    """
    Type for a reference to a LINK.

    :ivar from_point_ref: Start POINT of LINK.
    :ivar to_point_ref: End POINT of LINK.
    :ivar type_of_link_ref:
    :ivar vehicle_mode:
    :ivar name_of_class: Type of LINK.
    :ivar created: Date reference was first created.
    :ivar changed: Date reference was last changed.
    :ivar version: Version number of referenced entity.
    """
    from_point_ref: PointRefStructure = field(
        metadata={
            "name": "FromPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    to_point_ref: PointRefStructure = field(
        metadata={
            "name": "ToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    type_of_link_ref: Optional[TypeOfLinkRef] = field(
        default=None,
        metadata={
            "name": "TypeOfLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_mode: Optional[AllModesEnumeration] = field(
        default=None,
        metadata={
            "name": "VehicleMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
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
