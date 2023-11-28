from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.type_of_concession import TypeOfConcession
from netex.type_of_concession_ref import TypeOfConcessionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfConcessionsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of TYPE OF CONCESSIONs.
    """
    class Meta:
        name = "typeOfConcessions_RelStructure"

    type_of_concession_ref_or_type_of_concession: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TypeOfConcessionRef",
                    "type": TypeOfConcessionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfConcession",
                    "type": TypeOfConcession,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
