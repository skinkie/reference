from dataclasses import dataclass
from .site_entrance_version_structure import SiteEntranceVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOfInterestVehicleEntranceVersionStructure(
    SiteEntranceVersionStructure
):
    class Meta:
        name = "PointOfInterestVehicleEntrance_VersionStructure"
