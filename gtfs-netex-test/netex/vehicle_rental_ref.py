from dataclasses import dataclass

from .vehicle_rental_mode_of_operation_ref_structure import VehicleRentalModeOfOperationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehicleRentalRef(VehicleRentalModeOfOperationRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
