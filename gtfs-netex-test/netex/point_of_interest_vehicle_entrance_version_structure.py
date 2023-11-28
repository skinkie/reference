from dataclasses import dataclass
from netex.site_entrance_version_structure import SiteEntranceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOfInterestVehicleEntranceVersionStructure(SiteEntranceVersionStructure):
    """
    Type for a POINT OF INTEREST VEHICLE ENTRANCE.
    """
    class Meta:
        name = "PointOfInterestVehicleEntrance_VersionStructure"
