from dataclasses import dataclass, field
from typing import Union

from .access_space import AccessSpace
from .access_space_ref import AccessSpaceRef
from .containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class AccessSpacesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "accessSpaces_RelStructure"

    access_space_ref_or_access_space: list[Union[AccessSpaceRef, AccessSpace]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AccessSpaceRef",
                    "type": AccessSpaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessSpace",
                    "type": AccessSpace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
