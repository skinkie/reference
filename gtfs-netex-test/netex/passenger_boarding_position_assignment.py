from dataclasses import dataclass

from .deck_entrance_assignments_rel_structure import PassengerBoardingPositionAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PassengerBoardingPositionAssignment(PassengerBoardingPositionAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
