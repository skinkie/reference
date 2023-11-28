from dataclasses import dataclass, field
from netex.topographic_place_version_structure import TopographicPlaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TopographicPlace(TopographicPlaceVersionStructure):
    """A town, city, village, suburb, quarter or other name settlement within a
    country.

    Provides a Gazetteer of Transport related place names.

    :ivar id: Identifier of TOPOGRAPHIC PLACE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
