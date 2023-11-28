from dataclasses import dataclass, field
from netex.stop_place_version_structure import StopPlaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StopPlace(StopPlaceVersionStructure):
    """Version of a named place where public transport may be accessed.

    May be a building complex (e.g. a station) or an on-street location.

    :ivar id: Identifier of STOP PLACE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
