from dataclasses import dataclass
from .vehicle_meeting_place_ref_structure import (
    VehicleMeetingPlaceRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleMeetingPlaceRef(VehicleMeetingPlaceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
