from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.type_of_service import TypeOfService

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypesOfServiceInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of TYPE OF SERVICE.
    """
    class Meta:
        name = "typesOfServiceInFrame_RelStructure"

    type_of_service: List[TypeOfService] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
