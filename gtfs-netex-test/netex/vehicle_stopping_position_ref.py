from dataclasses import dataclass
from netex.vehicle_stopping_position_ref_structure import VehicleStoppingPositionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleStoppingPositionRef(VehicleStoppingPositionRefStructure):
    """
    Reference to a VEHICLE STOPPING POSITION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
