from dataclasses import dataclass
from .chauffeured_vehicle_service_version_structure import (
    ChauffeuredVehicleServiceVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ChauffeuredVehicleService(ChauffeuredVehicleServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
