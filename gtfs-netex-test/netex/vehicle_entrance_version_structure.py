from dataclasses import dataclass, field
from typing import Optional
from .site_entrance_version_structure import SiteEntranceVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleEntranceVersionStructure(SiteEntranceVersionStructure):
    class Meta:
        name = "VehicleEntrance_VersionStructure"

    public: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Public",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
