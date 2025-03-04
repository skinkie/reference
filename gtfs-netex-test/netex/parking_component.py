from dataclasses import dataclass

from .parking_component_version_structure import ParkingComponentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ParkingComponent(ParkingComponentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
