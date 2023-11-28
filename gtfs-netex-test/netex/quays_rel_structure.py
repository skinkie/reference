from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.quay import Quay
from netex.quay_ref import QuayRef
from netex.taxi_stand_ref import TaxiStandRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class QuaysRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of QUAYs.
    """
    class Meta:
        name = "quays_RelStructure"

    taxi_stand_ref_or_quay_ref_or_quay: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TaxiStandRef",
                    "type": TaxiStandRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QuayRef",
                    "type": QuayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Quay",
                    "type": Quay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
