from dataclasses import dataclass, field
from netex.taxi_stand_version_structure import TaxiStandVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TaxiStand(TaxiStandVersionStructure):
    """A set of spots where any taxi is able to safely stop for a short period of
    time to load passengers.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
