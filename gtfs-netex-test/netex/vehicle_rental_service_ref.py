from dataclasses import dataclass
from netex.vehicle_rental_service_ref_structure import VehicleRentalServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleRentalServiceRef(VehicleRentalServiceRefStructure):
    """Identifier of an VEHICLE RENTAL SERVICE.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
