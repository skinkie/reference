from dataclasses import dataclass, field
from netex.vehicle_rental_service_version_structure import VehicleRentalServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleRentalService(VehicleRentalServiceVersionStructure):
    """A transport service offer related to VEHICLE RENTAL.

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
