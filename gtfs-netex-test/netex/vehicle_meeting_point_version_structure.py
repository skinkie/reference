from dataclasses import dataclass

from .point_version_structure import PointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleMeetingPointVersionStructure(PointVersionStructure):
    class Meta:
        name = "VehicleMeetingPoint_VersionStructure"
