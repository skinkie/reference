from dataclasses import dataclass, field
from typing import Union

from .access import Access
from .access_ref import AccessRef
from .containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class AccessesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "accesses_RelStructure"

    access_ref_or_access: list[Union[AccessRef, Access]] = field(
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
        },
    )
