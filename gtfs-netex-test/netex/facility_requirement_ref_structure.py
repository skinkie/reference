from dataclasses import dataclass
from .vehicle_requirement_ref_structure import VehicleRequirementRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FacilityRequirementRefStructure(VehicleRequirementRefStructure):
    value: RestrictedVar
