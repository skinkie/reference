from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.type_of_usage_parameter import TypeOfUsageParameter
from netex.type_of_usage_parameter_ref import TypeOfUsageParameterRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfUsageParametersRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of TYPE OF USAGE PARAMETERs.
    """
    class Meta:
        name = "typeOfUsageParameters_RelStructure"

    type_of_usage_parameter_ref_or_type_of_usage_parameter: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TypeOfUsageParameterRef",
                    "type": TypeOfUsageParameterRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfUsageParameter",
                    "type": TypeOfUsageParameter,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
