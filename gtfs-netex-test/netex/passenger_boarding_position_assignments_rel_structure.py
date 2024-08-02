from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .deck_entrance_assignments_rel_structure import DeckEntranceAssignment
from .passenger_boarding_position_assignment import PassengerBoardingPositionAssignment
from .passenger_boarding_position_assignment_ref import PassengerBoardingPositionAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerBoardingPositionAssignmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "passengerBoardingPositionAssignments_RelStructure"

    passenger_boarding_position_assignment_ref_or_passenger_boarding_position_assignment_or_deck_entrance_assignment: List[Union[PassengerBoardingPositionAssignmentRef, PassengerBoardingPositionAssignment, DeckEntranceAssignment]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PassengerBoardingPositionAssignmentRef",
                    "type": PassengerBoardingPositionAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerBoardingPositionAssignment",
                    "type": PassengerBoardingPositionAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeckEntranceAssignment",
                    "type": DeckEntranceAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
