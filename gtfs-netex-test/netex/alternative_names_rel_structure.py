from dataclasses import dataclass, field
from typing import List
from netex.alternative_name import AlternativeName
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AlternativeNamesRelStructure(StrictContainmentAggregationStructure):
    """
    Type for list of ALTERNATIVE NAMEs.

    :ivar alternative_name: ALTERNATIVE NAME for Element.
    """
    class Meta:
        name = "alternativeNames_RelStructure"

    alternative_name: List[AlternativeName] = field(
        default_factory=list,
        metadata={
            "name": "AlternativeName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
