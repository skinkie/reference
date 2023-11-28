from dataclasses import dataclass, field
from typing import List
from netex.alternative_texts_rel_structure import ValidityTriggerVersionStructure
from netex.containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ValidityTriggersRelStructure(ContainmentAggregationStructure):
    """
    A collection of one or more VALIDITY TRIGGERs.

    :ivar validity_trigger: External event defining a VALIDITY
        CONDITION. E.g. exceptional flow of a river, bad weather, Road
        closure for works.
    """
    class Meta:
        name = "validityTriggers_RelStructure"

    validity_trigger: List[ValidityTriggerVersionStructure] = field(
        default_factory=list,
        metadata={
            "name": "ValidityTrigger",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
