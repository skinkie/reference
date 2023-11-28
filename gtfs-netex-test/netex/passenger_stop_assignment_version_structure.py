from dataclasses import dataclass, field
from typing import Optional
from netex.boarding_position import BoardingPosition
from netex.boarding_position_ref import BoardingPositionRef
from netex.quay import Quay
from netex.quay_ref import QuayRef
from netex.stop_assignment_version_structure import StopAssignmentVersionStructure
from netex.stop_place import StopPlace
from netex.stop_place_ref import StopPlaceRef
from netex.taxi_rank_ref import TaxiRankRef
from netex.taxi_stand_ref import TaxiStandRef
from netex.train_stop_assignments_rel_structure import TrainStopAssignmentsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PassengerStopAssignmentVersionStructure(StopAssignmentVersionStructure):
    """
    Type for a PASSENGER STOP ASSIGNMENT.

    :ivar taxi_rank_ref_or_stop_place_ref_or_stop_place:
    :ivar taxi_stand_ref_or_quay_ref_or_quay:
    :ivar boarding_position_ref_or_boarding_position:
    :ivar train_elements: Train elements to which SCHEDULED STOP POINT
        is to be assigned.
    """
    class Meta:
        name = "PassengerStopAssignment_VersionStructure"

    taxi_rank_ref_or_stop_place_ref_or_stop_place: Optional[object] = field(
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
        }
    )
    taxi_stand_ref_or_quay_ref_or_quay: Optional[object] = field(
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
        }
    )
    boarding_position_ref_or_boarding_position: Optional[object] = field(
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
        }
    )
    train_elements: Optional[TrainStopAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "trainElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
