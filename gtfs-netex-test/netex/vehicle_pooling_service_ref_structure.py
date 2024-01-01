from dataclasses import dataclass
from .common_vehicle_service_ref_structure import (
    CommonVehicleServiceRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehiclePoolingServiceRefStructure(CommonVehicleServiceRefStructure):
    value: RestrictedVar
