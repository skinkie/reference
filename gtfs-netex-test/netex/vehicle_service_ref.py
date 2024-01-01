from dataclasses import dataclass
from .vehicle_service_ref_structure import VehicleServiceRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleServiceRef(VehicleServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
