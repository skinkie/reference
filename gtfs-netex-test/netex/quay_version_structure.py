from dataclasses import dataclass, field
from typing import Optional
from netex.boarding_positions_rel_structure import BoardingPositionsRelStructure
from netex.compass_bearing8_enumeration import CompassBearing8Enumeration
from netex.destination_display_views_rel_structure import DestinationDisplayViewsRelStructure
from netex.quay_ref_structure import QuayRefStructure
from netex.quay_type_enumeration import QuayTypeEnumeration
from netex.stop_place_space_version_structure import StopPlaceSpaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class QuayVersionStructure(StopPlaceSpaceVersionStructure):
    """
    Type for QUAY.

    :ivar public_code: Pubic identifier code of QUAY.
    :ivar plate_code: Plate number for QUAY. An arbitrary asset number
        that may be placed on stop to identify it.
    :ivar short_code: A 20 bit number used for wireless cleardown of
        stop displays by some AVL systems.
    :ivar destinations: Default Destination headings for QUAY.
    :ivar compass_bearing: Heading of QUAY relative to street.
    :ivar compass_octant: Heading of QUAY relative to street in Octants.
    :ivar quay_type: Type of QUAY.
    :ivar parent_quay_ref: if QUAY is a subzone of another QUAY,
        identifies parent.
    :ivar boarding_positions: BOARDING POSITIONs within QUAY.
    """
    class Meta:
        name = "Quay_VersionStructure"

    public_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    plate_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    short_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "ShortCode",
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
    compass_bearing: Optional[float] = field(
        default=None,
        metadata={
            "name": "CompassBearing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    compass_octant: Optional[CompassBearing8Enumeration] = field(
        default=None,
        metadata={
            "name": "CompassOctant",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    quay_type: Optional[QuayTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "QuayType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parent_quay_ref: Optional[QuayRefStructure] = field(
        default=None,
        metadata={
            "name": "ParentQuayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    boarding_positions: Optional[BoardingPositionsRelStructure] = field(
        default=None,
        metadata={
            "name": "boardingPositions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
