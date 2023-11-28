from dataclasses import dataclass, field
from typing import Optional
from netex.all_modes_enumeration import AllModesEnumeration
from netex.place_ref_structure import PlaceRefStructure
from netex.point_ref_structure import PointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessEndStructure:
    """
    Type for ACCESS link end.

    :ivar transport_mode: Identifier of MODE of end point of ACCESS
        link. Default is all modes.
    :ivar place_ref: Identifier of a PLACE at end point of ACCESS link.
    :ivar point_ref: Identifier of end point of ACCESS link.
    """
    transport_mode: Optional[AllModesEnumeration] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    place_ref: Optional[PlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "PlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_ref: Optional[PointRefStructure] = field(
        default=None,
        metadata={
            "name": "PointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
