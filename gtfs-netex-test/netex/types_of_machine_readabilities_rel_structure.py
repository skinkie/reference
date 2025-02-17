from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .type_of_machine_readability_ref import TypeOfMachineReadabilityRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypesOfMachineReadabilitiesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "typesOfMachineReadabilities_RelStructure"

    type_of_machine_readability_ref: list[TypeOfMachineReadabilityRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfMachineReadabilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
