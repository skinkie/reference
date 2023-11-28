from dataclasses import dataclass, field
from netex.garage_version_structure import GarageVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Garage(GarageVersionStructure):
    """A facility used for parking and maintaining vehicles.

    PARKING POINTs in a GARAGE are called GARAGE POINTs.

    :ivar id: Identifier of GARAGE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
