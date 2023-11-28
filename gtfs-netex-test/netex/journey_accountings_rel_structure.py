from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.journey_accounting import JourneyAccounting
from netex.journey_accounting_ref import JourneyAccountingRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyAccountingsRelStructure(ContainmentAggregationStructure):
    """
    JOURNEY ACCOUNTING associated with entity.
    """
    class Meta:
        name = "journeyAccountings_RelStructure"

    journey_accounting_ref_or_journey_accounting: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "JourneyAccountingRef",
                    "type": JourneyAccountingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyAccounting",
                    "type": JourneyAccounting,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
