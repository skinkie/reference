from dataclasses import dataclass

from .site_entrance_version_structure import SiteEntranceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PointOfInterestVehicleEntranceVersionStructure(SiteEntranceVersionStructure):
    class Meta:
        name = "PointOfInterestVehicleEntrance_VersionStructure"
