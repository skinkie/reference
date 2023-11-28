from dataclasses import dataclass
from netex.vehicle_meeting_point_ref_structure import VehicleMeetingPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleMeetingPointRef(VehicleMeetingPointRefStructure):
    """Reference to a VEHICLE MEETING POINT.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
