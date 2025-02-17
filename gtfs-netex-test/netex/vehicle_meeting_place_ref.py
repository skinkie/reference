from dataclasses import dataclass

from .vehicle_meeting_place_ref_structure import VehicleMeetingPlaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehicleMeetingPlaceRef(VehicleMeetingPlaceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
