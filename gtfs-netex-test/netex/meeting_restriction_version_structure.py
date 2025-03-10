from dataclasses import dataclass, field
from typing import Optional

from .infrastructure_link_restriction_version_structure import InfrastructureLinkRestrictionVersionStructure
from .transport_type_ref_structure import TransportTypeRefStructure
from .vehicle_type_ref_structure import VehicleTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class MeetingRestrictionVersionStructure(InfrastructureLinkRestrictionVersionStructure):
    class Meta:
        name = "MeetingRestriction_VersionStructure"

    for_vehicle_type_ref: Optional[VehicleTypeRefStructure] = field(
        default=None,
        metadata={
            "name": "ForVehicleTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    against_vehicle_type_ref: Optional[TransportTypeRefStructure] = field(
        default=None,
        metadata={
            "name": "AgainstVehicleTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
