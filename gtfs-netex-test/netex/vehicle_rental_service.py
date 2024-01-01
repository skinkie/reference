from dataclasses import dataclass
from .vehicle_rental_service_version_structure import (
    VehicleRentalServiceVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleRentalService(VehicleRentalServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
