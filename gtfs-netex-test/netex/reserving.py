from dataclasses import dataclass, field
from netex.reserving_version_structure import ReservingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Reserving(ReservingVersionStructure):
    """
    The number and characteristics of persons entitled to use the public transport
    service instead of the original customer.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
