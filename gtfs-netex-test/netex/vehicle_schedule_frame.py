from dataclasses import dataclass, field
from netex.vehicle_schedule_version_frame_structure import VehicleScheduleVersionFrameStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleScheduleFrame(VehicleScheduleVersionFrameStructure):
    """
    A coherent set of Vehicle Scheduling data to which the same VALIDITY CONDITIONs
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
