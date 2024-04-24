from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .passenger_space import PassengerSpace
from .passenger_space_ref import PassengerSpaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerSpacesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "passengerSpaces_RelStructure"

    passenger_space_ref_or_passenger_space: List[Union[PassengerSpaceRef, PassengerSpace]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PassengerSpaceRef",
                    "type": PassengerSpaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerSpace",
                    "type": PassengerSpace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
