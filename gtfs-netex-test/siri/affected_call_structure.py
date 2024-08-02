from dataclasses import dataclass, field
from typing import List, Optional, Union

from .actual_arrival_time import ActualArrivalTime
from .actual_departure_time import ActualDepartureTime
from .affected_interchange_structure import AffectedInterchangeStructure
from .affected_stop_point_structure import AffectedStopPointStructure
from .aimed_arrival_time import AimedArrivalTime
from .aimed_departure_time import AimedDepartureTime
from .aimed_headway_interval import AimedHeadwayInterval
from .arrival_boarding_activity import ArrivalBoardingActivity
from .arrival_platform_name import ArrivalPlatformName
from .arrival_status import ArrivalStatus
from .departure_boarding_activity import DepartureBoardingActivity
from .departure_platform_name import DeparturePlatformName
from .departure_status import DepartureStatus
from .expected_arrival_time import ExpectedArrivalTime
from .expected_departure_time import ExpectedDepartureTime
from .expected_headway_interval import ExpectedHeadwayInterval
from .location_structure import LocationStructure
from .natural_language_string_structure import NaturalLanguageStringStructure
from .route_point_type_enumeration import RoutePointTypeEnumeration
from .timing_point import TimingPoint
from .vehicle_at_stop import VehicleAtStop

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AffectedCallStructure(AffectedStopPointStructure):
    order: Optional[int] = field(
        default=None,
        metadata={
            "name": "Order",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    call_condition: List[RoutePointTypeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "CallCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_at_stop: Optional[VehicleAtStop] = field(
        default=None,
        metadata={
            "name": "VehicleAtStop",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_location_at_stop: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "VehicleLocationAtStop",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
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
    aimed_arrival_time: Optional[AimedArrivalTime] = field(
        default=None,
        metadata={
            "name": "AimedArrivalTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    actual_arrival_time_or_expected_arrival_time: Optional[Union[ActualArrivalTime, ExpectedArrivalTime]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ActualArrivalTime",
                    "type": ActualArrivalTime,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "ExpectedArrivalTime",
                    "type": ExpectedArrivalTime,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
    arrival_status: Optional[ArrivalStatus] = field(
        default=None,
        metadata={
            "name": "ArrivalStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    arrival_platform_name: List[ArrivalPlatformName] = field(
        default_factory=list,
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
    aimed_departure_time: Optional[AimedDepartureTime] = field(
        default=None,
        metadata={
            "name": "AimedDepartureTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    actual_departure_time_or_expected_departure_time: Optional[Union[ActualDepartureTime, ExpectedDepartureTime]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ActualDepartureTime",
                    "type": ActualDepartureTime,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "ExpectedDepartureTime",
                    "type": ExpectedDepartureTime,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
    departure_status: Optional[DepartureStatus] = field(
        default=None,
        metadata={
            "name": "DepartureStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    departure_platform_name: List[DeparturePlatformName] = field(
        default_factory=list,
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
    aimed_headway_interval: Optional[AimedHeadwayInterval] = field(
        default=None,
        metadata={
            "name": "AimedHeadwayInterval",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    expected_headway_interval: Optional[ExpectedHeadwayInterval] = field(
        default=None,
        metadata={
            "name": "ExpectedHeadwayInterval",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    affected_interchanges: Optional["AffectedCallStructure.AffectedInterchanges"] = field(
        default=None,
        metadata={
            "name": "AffectedInterchanges",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass(kw_only=True)
    class AffectedInterchanges:
        affected_interchange: List[AffectedInterchangeStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedInterchange",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
