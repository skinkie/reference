from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional, Union

from .aimed_arrival_time import AimedArrivalTime
from .aimed_departure_time import AimedDepartureTime
from .aimed_headway_interval import AimedHeadwayInterval
from .aimed_latest_passenger_access_time import AimedLatestPassengerAccessTime
from .arrival_boarding_activity import ArrivalBoardingActivity
from .arrival_formation_assignment import ArrivalFormationAssignment
from .arrival_operator_refs import ArrivalOperatorRefs
from .arrival_platform_name import ArrivalPlatformName
from .departure_boarding_activity import DepartureBoardingActivity
from .departure_formation_assignment import DepartureFormationAssignment
from .departure_operator_refs import DepartureOperatorRefs
from .departure_platform_name import DeparturePlatformName
from .extensions_1 import Extensions1
from .from_service_journey_interchange_structure import FromServiceJourneyInterchangeStructure
from .natural_language_string_structure import NaturalLanguageStringStructure
from .order import Order
from .planned_stop_assignment_structure import PlannedStopAssignmentStructure
from .stop_point_name import StopPointName
from .stop_point_ref import StopPointRef
from .targeted_interchange_structure import TargetedInterchangeStructure
from .timing_point import TimingPoint
from .to_service_journey_interchange_structure import ToServiceJourneyInterchangeStructure
from .visit_number import VisitNumber

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class DatedCallStructure:
    stop_point_ref: StopPointRef = field(
        metadata={
            "name": "StopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    visit_number: Optional[VisitNumber] = field(
        default=None,
        metadata={
            "name": "VisitNumber",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    order: Optional[Order] = field(
        default=None,
        metadata={
            "name": "Order",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_point_name: List[StopPointName] = field(
        default_factory=list,
        metadata={
            "name": "StopPointName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extra_call_or_cancellation: Optional[Union["DatedCallStructure.ExtraCall", "DatedCallStructure.Cancellation"]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ExtraCall",
                    "type": ForwardRef("DatedCallStructure.ExtraCall"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "Cancellation",
                    "type": ForwardRef("DatedCallStructure.Cancellation"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
    timing_point: Optional[TimingPoint] = field(
        default=None,
        metadata={
            "name": "TimingPoint",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    boarding_stretch: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BoardingStretch",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    request_stop: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RequestStop",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    origin_display: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "OriginDisplay",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    destination_display: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "DestinationDisplay",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    call_note: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "CallNote",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    aimed_arrival_time: Optional[AimedArrivalTime] = field(
        default=None,
        metadata={
            "name": "AimedArrivalTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    arrival_platform_name: Optional[ArrivalPlatformName] = field(
        default=None,
        metadata={
            "name": "ArrivalPlatformName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    arrival_boarding_activity: Optional[ArrivalBoardingActivity] = field(
        default=None,
        metadata={
            "name": "ArrivalBoardingActivity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    arrival_stop_assignment: List[PlannedStopAssignmentStructure] = field(
        default_factory=list,
        metadata={
            "name": "ArrivalStopAssignment",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    arrival_formation_assignment: List[ArrivalFormationAssignment] = field(
        default_factory=list,
        metadata={
            "name": "ArrivalFormationAssignment",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    arrival_operator_refs: List[ArrivalOperatorRefs] = field(
        default_factory=list,
        metadata={
            "name": "ArrivalOperatorRefs",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    aimed_departure_time: Optional[AimedDepartureTime] = field(
        default=None,
        metadata={
            "name": "AimedDepartureTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    departure_platform_name: Optional[DeparturePlatformName] = field(
        default=None,
        metadata={
            "name": "DeparturePlatformName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    departure_boarding_activity: Optional[DepartureBoardingActivity] = field(
        default=None,
        metadata={
            "name": "DepartureBoardingActivity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    departure_stop_assignment: List[PlannedStopAssignmentStructure] = field(
        default_factory=list,
        metadata={
            "name": "DepartureStopAssignment",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    departure_formation_assignment: List[DepartureFormationAssignment] = field(
        default_factory=list,
        metadata={
            "name": "DepartureFormationAssignment",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    departure_operator_refs: List[DepartureOperatorRefs] = field(
        default_factory=list,
        metadata={
            "name": "DepartureOperatorRefs",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    aimed_latest_passenger_access_time: Optional[AimedLatestPassengerAccessTime] = field(
        default=None,
        metadata={
            "name": "AimedLatestPassengerAccessTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    aimed_headway_interval: Optional[AimedHeadwayInterval] = field(
        default=None,
        metadata={
            "name": "AimedHeadwayInterval",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    targeted_interchange: List[TargetedInterchangeStructure] = field(
        default_factory=list,
        metadata={
            "name": "TargetedInterchange",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    from_service_journey_interchange: List[FromServiceJourneyInterchangeStructure] = field(
        default_factory=list,
        metadata={
            "name": "FromServiceJourneyInterchange",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    to_service_journey_interchange: List[ToServiceJourneyInterchangeStructure] = field(
        default_factory=list,
        metadata={
            "name": "ToServiceJourneyInterchange",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass(kw_only=True)
    class ExtraCall:
        value: bool = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class Cancellation:
        value: bool = field(
            metadata={
                "required": True,
            }
        )
