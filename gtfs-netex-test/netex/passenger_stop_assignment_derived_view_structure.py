from dataclasses import dataclass, field
from typing import Optional
from netex.derived_view_structure import DerivedViewStructure
from netex.dynamic_stop_assignment_ref import DynamicStopAssignmentRef
from netex.multilingual_string import MultilingualString
from netex.passenger_stop_assignment_ref import PassengerStopAssignmentRef
from netex.quay_ref_structure import QuayRefStructure
from netex.stop_place_ref import StopPlaceRef
from netex.taxi_rank_ref import TaxiRankRef
from netex.vehicle_journey_stop_assignment_ref import VehicleJourneyStopAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PassengerStopAssignmentDerivedViewStructure(DerivedViewStructure):
    """
    Type for a PASSENGER STOP POINT ASSIGNMENT VIEW.

    :ivar
        vehicle_journey_stop_assignment_ref_or_dynamic_stop_assignment_ref_or_passenger_stop_assignment_ref:
    :ivar taxi_rank_ref_or_stop_place_ref:
    :ivar quay_ref: QUAY to which SCHEDULED STOP POINT is to be
        assigned.
    :ivar quay_name: Name of QUAY or platform to which the SCHEDULED
        STOP POINT is assigned.
    :ivar label:
    :ivar order: Order of Assignment.
    """
    class Meta:
        name = "PassengerStopAssignment_DerivedViewStructure"

    vehicle_journey_stop_assignment_ref_or_dynamic_stop_assignment_ref_or_passenger_stop_assignment_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleJourneyStopAssignmentRef",
                    "type": VehicleJourneyStopAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DynamicStopAssignmentRef",
                    "type": DynamicStopAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerStopAssignmentRef",
                    "type": PassengerStopAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    taxi_rank_ref_or_stop_place_ref: Optional[object] = field(
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
            ),
        }
    )
    quay_ref: Optional[QuayRefStructure] = field(
        default=None,
        metadata={
            "name": "QuayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    quay_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "QuayName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    label: Optional[str] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
