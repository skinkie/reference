from dataclasses import dataclass
from .vehicle_entrance_ref_structure import VehicleEntranceRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleEntranceRef(VehicleEntranceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
