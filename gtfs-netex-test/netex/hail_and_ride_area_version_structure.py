from dataclasses import dataclass, field
from typing import Optional
from netex.compass_bearing16_enumeration import CompassBearing16Enumeration
from netex.destination_display_views_rel_structure import DestinationDisplayViewsRelStructure
from netex.flexible_quay_version_structure import FlexibleQuayVersionStructure
from netex.point_ref_structure import PointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class HailAndRideAreaVersionStructure(FlexibleQuayVersionStructure):
    """
    Type for a HAIL AND RIDE AREA.

    :ivar bearing_compass: Bearing of Road at point in compass octants
        to North.
    :ivar bearing_degrees: Bearing of Road in absolute degrees against
        North.
    :ivar destinations: Destination headings for HAIL AND RIDE AREA.
    :ivar start_point_ref: Start of HAIL AND RIDE section.
    :ivar end_point_ref: End of HAIL AND RIDE section.
    """
    class Meta:
        name = "HailAndRideArea_VersionStructure"

    bearing_compass: Optional[CompassBearing16Enumeration] = field(
        default=None,
        metadata={
            "name": "BearingCompass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    bearing_degrees: Optional[int] = field(
        default=None,
        metadata={
            "name": "BearingDegrees",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    destinations: Optional[DestinationDisplayViewsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_point_ref: PointRefStructure = field(
        metadata={
            "name": "StartPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    end_point_ref: PointRefStructure = field(
        metadata={
            "name": "EndPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
