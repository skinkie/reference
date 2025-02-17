from dataclasses import dataclass

from .vehicle_pooling_meeting_place_ref_structure import VehiclePoolingMeetingPlaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehiclePoolingMeetingPlaceRef(VehiclePoolingMeetingPlaceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
