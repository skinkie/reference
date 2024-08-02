from dataclasses import dataclass

from .deck_entrance_assignments_rel_structure import PassengerBoardingPositionAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerBoardingPositionAssignmentAbstract(PassengerBoardingPositionAssignmentVersionStructure):
    class Meta:
        name = "PassengerBoardingPositionAssignment_"
        namespace = "http://www.netex.org.uk/netex"
