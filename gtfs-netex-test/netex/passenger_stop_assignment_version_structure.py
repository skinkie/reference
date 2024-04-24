from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional, Union

from .boarding_position import BoardingPosition
from .boarding_position_ref import BoardingPositionRef
from .quay import Quay
from .quay_ref import QuayRef
from .stop_assignment_version_structure import StopAssignmentVersionStructure
from .stop_place import StopPlace
from .stop_place_ref import StopPlaceRef
from .taxi_rank_ref import TaxiRankRef
from .taxi_stand_ref import TaxiStandRef
from .train_stop_assignments_rel_structure import TrainStopAssignmentsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerStopAssignmentVersionStructure(StopAssignmentVersionStructure):
    class Meta:
        name = "PassengerStopAssignment_VersionStructure"

    taxi_rank_ref_or_stop_place_ref_or_stop_place: Optional[Union[TaxiRankRef, StopPlaceRef, StopPlace]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TaxiRankRef",
                    "type": TaxiRankRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlaceRef",
                    "type": StopPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlace",
                    "type": StopPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    taxi_stand_ref_or_quay_ref_or_quay: Optional[Union[TaxiStandRef, QuayRef, Quay]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TaxiStandRef",
                    "type": TaxiStandRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QuayRef",
                    "type": QuayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Quay",
                    "type": Quay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    boarding_position_ref_or_boarding_position: Optional[Union[BoardingPositionRef, BoardingPosition]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "BoardingPositionRef",
                    "type": BoardingPositionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BoardingPosition",
                    "type": BoardingPosition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    train_stop_assignments_or_train_elements: List[Union["PassengerStopAssignmentVersionStructure.TrainStopAssignments", "PassengerStopAssignmentVersionStructure.TrainElements"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "trainStopAssignments",
                    "type": ForwardRef("PassengerStopAssignmentVersionStructure.TrainStopAssignments"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "trainElements",
                    "type": ForwardRef("PassengerStopAssignmentVersionStructure.TrainElements"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class TrainStopAssignments(TrainStopAssignmentsRelStructure):
        pass

    @dataclass(kw_only=True)
    class TrainElements(TrainStopAssignmentsRelStructure):
        pass
