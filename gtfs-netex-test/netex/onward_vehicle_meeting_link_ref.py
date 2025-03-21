from dataclasses import dataclass

from .vehicle_meeting_link_ref_structure import VehicleMeetingLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class OnwardVehicleMeetingLinkRef(VehicleMeetingLinkRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
