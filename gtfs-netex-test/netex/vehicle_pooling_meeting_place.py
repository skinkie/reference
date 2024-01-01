from dataclasses import dataclass
from .vehicle_pooling_meeting_place_version_structure import (
    VehiclePoolingMeetingPlaceVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehiclePoolingMeetingPlace(VehiclePoolingMeetingPlaceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
