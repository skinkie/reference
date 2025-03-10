from dataclasses import dataclass, field
from typing import Optional, Union

from .public_code_structure import PublicCodeStructure
from .stop_area_ref_structure import StopAreaRefStructure
from .topographic_place_ref import TopographicPlaceRef
from .topographic_place_view import TopographicPlaceView
from .zone_version_structure import ZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class StopAreaVersionStructure(ZoneVersionStructure):
    class Meta:
        name = "StopArea_VersionStructure"

    public_code: Optional[PublicCodeStructure] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parent_stop_area_ref: Optional[StopAreaRefStructure] = field(
        default=None,
        metadata={
            "name": "ParentStopAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    topographic_place_ref_or_topographic_place_view: Optional[Union[TopographicPlaceRef, TopographicPlaceView]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TopographicPlaceRef",
                    "type": TopographicPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TopographicPlaceView",
                    "type": TopographicPlaceView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
