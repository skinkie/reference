from dataclasses import dataclass

from .vehicle_stopping_position_ref_structure import VehicleStoppingPositionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehicleStoppingPositionRef(VehicleStoppingPositionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
