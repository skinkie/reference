from dataclasses import dataclass, field
from typing import List, Optional
from netex.line_section_point_type_enumeration import LineSectionPointTypeEnumeration
from netex.point_on_section_versioned_child_structure import PointOnSectionVersionedChildStructure
from netex.vehicle_mode_enumeration import VehicleModeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOnLineSectionVersionedChildStructure(PointOnSectionVersionedChildStructure):
    """
    Type for a  POINT on LINE SECTION.

    :ivar line_section_point_type: Classification of Point Member.
    :ivar show_as_accessible: Whether point is to be shown as
        Accessible.
    :ivar connecting_vehicle_modes: Connecting Vehicle Modes to show for
        Point if different from  point.
    """
    class Meta:
        name = "PointOnLineSection_VersionedChildStructure"

    line_section_point_type: Optional[LineSectionPointTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "LineSectionPointType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    show_as_accessible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ShowAsAccessible",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    connecting_vehicle_modes: List[VehicleModeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ConnectingVehicleModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
