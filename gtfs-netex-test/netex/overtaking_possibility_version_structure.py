from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.link_ref_structure import LinkRefStructure
from netex.network_restriction_version_structure import NetworkRestrictionVersionStructure
from netex.point_ref_structure import PointRefStructure
from netex.transport_type_ref_structure import TransportTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OvertakingPossibilityVersionStructure(NetworkRestrictionVersionStructure):
    """
    Type for an OVERTAKING POSSIBILITY.

    :ivar overtaking_width: Width at overtaking point.
    :ivar overtaking_on_link_ref: Identifier of an INFRASTRUCTURE LINK
        over which two vehicles of the specified VEHICLE TYPE may pass
        in the  directions of the link.
    :ivar overtaking_at_point_ref: Identifier of a point at which two
        vehicles of the specified VEHICLE TYPE may overtake or not
        overtake.
    :ivar overtaking_vehicle_type_ref: TYPE OF VEHICLE  that may
        overtake.
    :ivar overtaken_vehicle_type_ref: TYPE OF VEHICLE  that may be
        overtaken.
    """
    class Meta:
        name = "OvertakingPossibility_VersionStructure"

    overtaking_width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "OvertakingWidth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    overtaking_on_link_ref: LinkRefStructure = field(
        metadata={
            "name": "OvertakingOnLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    overtaking_at_point_ref: Optional[PointRefStructure] = field(
        default=None,
        metadata={
            "name": "OvertakingAtPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    overtaking_vehicle_type_ref: Optional[TransportTypeRefStructure] = field(
        default=None,
        metadata={
            "name": "OvertakingVehicleTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    overtaken_vehicle_type_ref: Optional[TransportTypeRefStructure] = field(
        default=None,
        metadata={
            "name": "OvertakenVehicleTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
