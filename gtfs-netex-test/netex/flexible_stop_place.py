from dataclasses import dataclass, field
from netex.flexible_stop_place_version_structure import FlexibleStopPlaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FlexibleStopPlace(FlexibleStopPlaceVersionStructure):
    """
    A named type of STOP PLACE for DRT comprising one or more flexible zones where
    vehicles may stop and where passengers may board or leave vehicles.

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
