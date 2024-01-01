from dataclasses import dataclass
from .taxi_rank_version_structure import TaxiRankVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TaxiRank(TaxiRankVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
