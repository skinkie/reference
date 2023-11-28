from dataclasses import dataclass, field
from typing import Optional
from netex.infrastructure_link_restriction_version_structure import InfrastructureLinkRestrictionVersionStructure
from netex.transport_type_ref_structure import TransportTypeRefStructure
from netex.vehicle_type_ref_structure import VehicleTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MeetingRestrictionVersionStructure(InfrastructureLinkRestrictionVersionStructure):
    """
    Type for MEETING RESTRICTION.

    :ivar for_vehicle_type_ref: Type of vehicle that may use forwards
        direction of INFRASTRUCTURE LINK. For a meeting restriction this
        is for the forward sense of the link. For overtaking possibility
        this is for the overtaking vehicle.
    :ivar against_vehicle_type_ref: Type of vehicle that may use
        backwards direction of INFRASTRUCTURE LINK. For a meeting
        restriction this is for the vehicle going in the  reveser sense
        of the link. For overtaking possibility this is for the vehicle
        being  overtaken.
    """
    class Meta:
        name = "MeetingRestriction_VersionStructure"

    for_vehicle_type_ref: Optional[VehicleTypeRefStructure] = field(
        default=None,
        metadata={
            "name": "ForVehicleTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    against_vehicle_type_ref: Optional[TransportTypeRefStructure] = field(
        default=None,
        metadata={
            "name": "AgainstVehicleTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
