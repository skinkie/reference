from dataclasses import dataclass
from netex.vehicle_meeting_link_ref_structure import VehicleMeetingLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OnwardVehicleMeetingLinkRef(VehicleMeetingLinkRefStructure):
    """Reference to a n Onward VEHICLE MEETING LINK.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
