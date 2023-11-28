from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.type_of_facility import TypeOfFacility
from netex.type_of_facility_ref import TypeOfFacilityRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypesOfFacilityRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of TYPE OF FACILITYs.
    """
    class Meta:
        name = "typesOfFacility_RelStructure"

    type_of_facility_ref_or_type_of_facility: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TypeOfFacilityRef",
                    "type": TypeOfFacilityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFacility",
                    "type": TypeOfFacility,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
