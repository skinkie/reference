from dataclasses import dataclass, field
from netex.vehicle_pooler_profile_version_structure import VehiclePoolerProfileVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehiclePoolerProfile(VehiclePoolerProfileVersionStructure):
    """A set of USER PARAMETERS characterising access rights to VEHICLE POOLING
    SERVICE.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
