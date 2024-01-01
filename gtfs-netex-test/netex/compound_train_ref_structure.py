from dataclasses import dataclass
from .vehicle_type_ref_structure import VehicleTypeRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CompoundTrainRefStructure(VehicleTypeRefStructure):
    value: RestrictedVar
