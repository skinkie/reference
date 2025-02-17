from dataclasses import dataclass

from .passenger_boarding_position_assignment_ref_structure import PassengerBoardingPositionAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TrainComponentStopAssignmentRefStructure(PassengerBoardingPositionAssignmentRefStructure):
    pass
