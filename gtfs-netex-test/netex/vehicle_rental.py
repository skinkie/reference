from dataclasses import dataclass
from .vehicle_rental_mode_of_operation_value_structure import (
    VehicleRentalModeOfOperationValueStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleRental(VehicleRentalModeOfOperationValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
