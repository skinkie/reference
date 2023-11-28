from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.taxi_stand import TaxiStand

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TaxiStandsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of TAXI STANDs.
    """
    class Meta:
        name = "taxiStands_RelStructure"

    taxi_stand: List[TaxiStand] = field(
        default_factory=list,
        metadata={
            "name": "TaxiStand",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
