from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.passenger_carrying_requirement import PassengerCarryingRequirement
from netex.passenger_carrying_requirement_ref import PassengerCarryingRequirementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PassengerCarryingRequirementsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of PASSENGER CARRYING Requirements.
    """
    class Meta:
        name = "passengerCarryingRequirements_RelStructure"

    passenger_carrying_requirement_ref_or_passenger_carrying_requirement: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PassengerCarryingRequirementRef",
                    "type": PassengerCarryingRequirementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerCarryingRequirement",
                    "type": PassengerCarryingRequirement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
