from dataclasses import dataclass
from netex.vehicle_schedule_frame_ref_structure import VehicleScheduleFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleScheduleFrameRef(VehicleScheduleFrameRefStructure):
    """
    Reference to a VEHICLE SCHEDULE FRAME.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
