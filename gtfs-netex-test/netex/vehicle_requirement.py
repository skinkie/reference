from dataclasses import dataclass

from .vehicle_requirement_version_structure import VehicleRequirementVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleRequirement(VehicleRequirementVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
