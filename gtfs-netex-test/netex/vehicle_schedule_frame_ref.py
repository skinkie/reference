from dataclasses import dataclass

from .vehicle_schedule_frame_ref_structure import VehicleScheduleFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehicleScheduleFrameRef(VehicleScheduleFrameRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
