from dataclasses import dataclass, field
from typing import Optional
from netex.site_entrance_version_structure import SiteEntranceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleEntranceVersionStructure(SiteEntranceVersionStructure):
    """
    Type for a VEHICLE ENTRANCE.

    :ivar public: Whether private vehicles can use this entrance.
    """
    class Meta:
        name = "VehicleEntrance_VersionStructure"

    public: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Public",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
