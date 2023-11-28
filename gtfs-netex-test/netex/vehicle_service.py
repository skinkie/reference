from dataclasses import dataclass, field
from netex.vehicle_service_version_structure import VehicleServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleService(VehicleServiceVersionStructure):
    """A work plan for a vehicle for a whole day, planned for a specific DAY TYPE.

    A VEHICLE SERVICE includes one or several VEHICLE SERVICE PARTs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
