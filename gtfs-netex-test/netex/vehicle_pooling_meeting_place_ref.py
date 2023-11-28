from dataclasses import dataclass
from netex.vehicle_pooling_meeting_place_ref_structure import VehiclePoolingMeetingPlaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehiclePoolingMeetingPlaceRef(VehiclePoolingMeetingPlaceRefStructure):
    """Reference to a VEHICLE POOLING MEETING PLACE.

    v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
