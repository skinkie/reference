from dataclasses import dataclass
from netex.vehicle_meeting_place_ref_structure import VehicleMeetingPlaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehiclePoolingMeetingPlaceRefStructure(VehicleMeetingPlaceRefStructure):
    """
    Type for a reference to a VEHICLE POOLING MEETING PLACE.
    """
