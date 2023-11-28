from dataclasses import dataclass, field
from typing import List
from netex.access import Access
from netex.access_ref import AccessRef
from netex.containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of ACCESS Links.
    """
    class Meta:
        name = "accesses_RelStructure"

    access_ref_or_access: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AccessRef",
                    "type": AccessRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Access",
                    "type": Access,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
