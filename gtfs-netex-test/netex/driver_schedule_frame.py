from dataclasses import dataclass

from .driver_schedule_version_frame_structure import DriverScheduleVersionFrameStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DriverScheduleFrame(DriverScheduleVersionFrameStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
