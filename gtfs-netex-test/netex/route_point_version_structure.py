from dataclasses import dataclass, field
from typing import Optional
from .point_version_structure import PointVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoutePointVersionStructure(PointVersionStructure):
    class Meta:
        name = "RoutePoint_VersionStructure"

    via_flag: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ViaFlag",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    border_crossing: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BorderCrossing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
