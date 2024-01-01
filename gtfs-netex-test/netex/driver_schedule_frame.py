from dataclasses import dataclass
from .driver_schedule_version_frame_structure import (
    DriverScheduleVersionFrameStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DriverScheduleFrame(DriverScheduleVersionFrameStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
