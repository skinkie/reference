from dataclasses import dataclass, field
from typing import List, Optional, Union

from xsdata.models.datatype import XmlDateTime

from .abstract_monitored_call_structure import AbstractMonitoredCallStructure
from .actual_arrival_time import ActualArrivalTime
from .actual_departure_time import ActualDepartureTime
from .aimed_arrival_time import AimedArrivalTime
from .aimed_departure_time import AimedDepartureTime
from .aimed_headway_interval import AimedHeadwayInterval
from .aimed_latest_passenger_access_time import AimedLatestPassengerAccessTime
from .arrival_boarding_activity import ArrivalBoardingActivity
from .arrival_cancellation_reason import ArrivalCancellationReason
from .arrival_formation_assignment import ArrivalFormationAssignment
from .arrival_operator_refs import ArrivalOperatorRefs
from .arrival_orientation_relative_to_quay import ArrivalOrientationRelativeToQuay
from .arrival_platform_name import ArrivalPlatformName
from .arrival_proximity_text import ArrivalProximityText
from .arrival_status import ArrivalStatus
from .departure_boarding_activity import DepartureBoardingActivity
from .departure_cancellation_reason import DepartureCancellationReason
from .departure_formation_assignment import DepartureFormationAssignment
from .departure_operator_refs import DepartureOperatorRefs
from .departure_orientation_relative_to_quay import DepartureOrientationRelativeToQuay
from .departure_platform_name import DeparturePlatformName
from .departure_proximity_text import DepartureProximityText
from .departure_status import DepartureStatus
from .expected_arrival_time import ExpectedArrivalTime
from .expected_departure_capacities import ExpectedDepartureCapacities
from .expected_departure_occupancy import ExpectedDepartureOccupancy
from .expected_departure_time import ExpectedDepartureTime
from .expected_headway_interval import ExpectedHeadwayInterval
from .expected_latest_passenger_access_time import ExpectedLatestPassengerAccessTime
from .extensions_1 import Extensions1
from .facility_change_element import FacilityChangeElement
from .facility_condition_element import FacilityConditionElement
from .formation_condition import FormationCondition
from .location_structure import LocationStructure
from .natural_language_string_structure import NaturalLanguageStringStructure
from .prediction_quality_structure import PredictionQualityStructure
from .recorded_departure_capacities import RecordedDepartureCapacities
from .recorded_departure_occupancy import RecordedDepartureOccupancy
from .situation_ref import SituationRef
from .stop_assignment_structure import StopAssignmentStructure
from .timing_point import TimingPoint
from .vehicle_at_stop import VehicleAtStop

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class MonitoredCallStructure(AbstractMonitoredCallStructure):
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
    reverses_at_stop: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReversesAtStop",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    platform_traversal: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PlatformTraversal",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    signal_status: Optional[str] = field(
        default=None,
        metadata={
            "name": "SignalStatus",
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
    call_note: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "CallNote",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    formation_condition: List[FormationCondition] = field(
        default_factory=list,
        metadata={
            "name": "FormationCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_condition_element: List[FacilityConditionElement] = field(
        default_factory=list,
        metadata={
            "name": "FacilityConditionElement",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_change_element: Optional[FacilityChangeElement] = field(
        default=None,
        metadata={
            "name": "FacilityChangeElement",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_ref: List[SituationRef] = field(
        default_factory=list,
        metadata={
            "name": "SituationRef",
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
    latest_expected_arrival_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LatestExpectedArrivalTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
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
    arrival_cancellation_reason: Optional[ArrivalCancellationReason] = field(
        default=None,
        metadata={
            "name": "ArrivalCancellationReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    arrival_proximity_text: Optional[ArrivalProximityText] = field(
        default=None,
        metadata={
            "name": "ArrivalProximityText",
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
    arrival_stop_assignment: List[StopAssignmentStructure] = field(
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
    arrival_orientation_relative_to_quay: List[ArrivalOrientationRelativeToQuay] = field(
        default_factory=list,
        metadata={
            "name": "ArrivalOrientationRelativeToQuay",
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
    provisional_expected_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ProvisionalExpectedDepartureTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    earliest_expected_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EarliestExpectedDepartureTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    expected_departure_prediction_quality: Optional[PredictionQualityStructure] = field(
        default=None,
        metadata={
            "name": "ExpectedDeparturePredictionQuality",
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
    expected_latest_passenger_access_time: Optional[ExpectedLatestPassengerAccessTime] = field(
        default=None,
        metadata={
            "name": "ExpectedLatestPassengerAccessTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
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
    departure_cancellation_reason: Optional[DepartureCancellationReason] = field(
        default=None,
        metadata={
            "name": "DepartureCancellationReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    departure_proximity_text: Optional[DepartureProximityText] = field(
        default=None,
        metadata={
            "name": "DepartureProximityText",
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
    departure_stop_assignment: List[StopAssignmentStructure] = field(
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
    departure_orientation_relative_to_quay: List[DepartureOrientationRelativeToQuay] = field(
        default_factory=list,
        metadata={
            "name": "DepartureOrientationRelativeToQuay",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    expected_departure_occupancy_or_expected_departure_capacities_or_recorded_departure_occupancy_or_recorded_departure_capacities: List[Union[ExpectedDepartureOccupancy, ExpectedDepartureCapacities, RecordedDepartureOccupancy, RecordedDepartureCapacities]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ExpectedDepartureOccupancy",
                    "type": ExpectedDepartureOccupancy,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "ExpectedDepartureCapacities",
                    "type": ExpectedDepartureCapacities,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "RecordedDepartureOccupancy",
                    "type": RecordedDepartureOccupancy,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "RecordedDepartureCapacities",
                    "type": RecordedDepartureCapacities,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
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
    distance_from_stop: Optional[int] = field(
        default=None,
        metadata={
            "name": "DistanceFromStop",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    number_of_stops_away: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfStopsAway",
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
