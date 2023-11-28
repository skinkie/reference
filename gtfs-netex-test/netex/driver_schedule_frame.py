from dataclasses import dataclass, field
from netex.driver_schedule_version_frame_structure import DriverScheduleVersionFrameStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DriverScheduleFrame(DriverScheduleVersionFrameStructure):
    """
    A coherent set of Driver Scheduling data to which the same VALIDITY CONDITIONs
    have been assigned.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
