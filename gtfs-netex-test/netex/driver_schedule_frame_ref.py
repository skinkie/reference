from dataclasses import dataclass

from .driver_schedule_frame_ref_structure import DriverScheduleFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DriverScheduleFrameRef(DriverScheduleFrameRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
