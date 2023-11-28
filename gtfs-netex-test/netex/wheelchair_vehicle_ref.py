from dataclasses import dataclass
from netex.wheelchair_vehicle_ref_structure import WheelchairVehicleRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class WheelchairVehicleRef(WheelchairVehicleRefStructure):
    """
    Reference to a WHEELCHAIR VEHICLE EQUIPMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
