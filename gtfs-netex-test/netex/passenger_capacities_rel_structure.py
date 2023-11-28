from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.passenger_capacity import PassengerCapacity
from netex.passenger_capacity_ref import PassengerCapacityRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PassengerCapacitiesRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of PASSENGER CAPACITY REQUIREMENTs.
    """
    class Meta:
        name = "passengerCapacities_RelStructure"

    passenger_capacity_ref_or_passenger_capacity: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PassengerCapacityRef",
                    "type": PassengerCapacityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerCapacity",
                    "type": PassengerCapacity,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
