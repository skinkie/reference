from dataclasses import dataclass
from netex.vehicle_meeting_place_ref_structure import VehicleMeetingPlaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleMeetingPlaceRef(VehicleMeetingPlaceRefStructure):
    """Reference to a VEHICLE MEETING PLACE.

    v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
