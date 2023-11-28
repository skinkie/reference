from dataclasses import dataclass
from netex.driver_schedule_frame_ref_structure import DriverScheduleFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DriverScheduleFrameRef(DriverScheduleFrameRefStructure):
    """
    Reference to a DRIVER SCHEDULE FRAME.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
