from dataclasses import dataclass, field
from typing import List, Union

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .passenger_capacity import PassengerCapacity
from .passenger_capacity_ref import PassengerCapacityRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerCapacitiesRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "passengerCapacities_RelStructure"

    passenger_capacity_ref_or_passenger_capacity: List[
        Union[PassengerCapacityRef, PassengerCapacity]
    ] = field(
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
        },
    )
