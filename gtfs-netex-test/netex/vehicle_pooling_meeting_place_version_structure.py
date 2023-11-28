from dataclasses import dataclass
from netex.vehicle_meeting_place_version_structure import VehicleMeetingPlaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehiclePoolingMeetingPlaceVersionStructure(VehicleMeetingPlaceVersionStructure):
    """
    Type for VEHICLE POOLING MEETING PLACE.
    """
    class Meta:
        name = "VehiclePoolingMeetingPlace_VersionStructure"
