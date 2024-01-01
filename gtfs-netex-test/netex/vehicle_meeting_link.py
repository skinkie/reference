from dataclasses import dataclass
from .vehicle_meeting_link_version_structure import (
    VehicleMeetingLinkVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleMeetingLink(VehicleMeetingLinkVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
