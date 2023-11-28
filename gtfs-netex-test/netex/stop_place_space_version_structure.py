from dataclasses import dataclass, field
from typing import Optional
from netex.multilingual_string import MultilingualString
from netex.site_entrances_rel_structure import SiteEntrancesRelStructure
from netex.stop_place_component_version_structure import StopPlaceComponentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StopPlaceSpaceVersionStructure(StopPlaceComponentVersionStructure):
    """
    Type for a STOP PLACE SPACE.

    :ivar boarding_use: Whether space can be used for boarding or en
        route to boarding. Default is true.
    :ivar alighting_use: Whether space can be used for alighting or en
        route to boarding. Default is true.
    :ivar label: Label for SPACE.
    :ivar entrances: ENTRANCEs to SPACE.
    """
    class Meta:
        name = "StopPlaceSpace_VersionStructure"

    boarding_use: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BoardingUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    alighting_use: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AlightingUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    label: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entrances: Optional[SiteEntrancesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
