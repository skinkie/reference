from dataclasses import dataclass, field
from netex.parking_version_structure import ParkingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Parking(ParkingVersionStructure):
    """A named place where Parking may be accessed.

    May be a building complex (e.g. a station) or an on-street location.

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
