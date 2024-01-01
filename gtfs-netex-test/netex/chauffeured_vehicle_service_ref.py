from dataclasses import dataclass
from .chauffeured_vehicle_service_ref_structure import (
    ChauffeuredVehicleServiceRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ChauffeuredVehicleServiceRef(ChauffeuredVehicleServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
