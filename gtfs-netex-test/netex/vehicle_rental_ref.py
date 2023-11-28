from dataclasses import dataclass
from netex.vehicle_rental_mode_of_operation_ref_structure import VehicleRentalModeOfOperationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleRentalRef(VehicleRentalModeOfOperationRefStructure):
    """Reference to a VEHICLE RENTAL MODE OF OPERATION.

    +V1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
