from dataclasses import dataclass, field
from netex.taxi_rank_version_structure import TaxiRankVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TaxiRank(TaxiRankVersionStructure):
    """A place comprising one or more locations where taxis may stop to pick up or
    set down passengersA place comprising one or more locations where taxis may
    stop to pick up or set down passengers.

    +v1.2.2

    :ivar id: Identifier of TAXI RANK.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
