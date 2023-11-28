from dataclasses import dataclass
from netex.taxi_rank_ref_structure import TaxiRankRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TaxiRankRef(TaxiRankRefStructure):
    """Reference to a TAXI RANK.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
