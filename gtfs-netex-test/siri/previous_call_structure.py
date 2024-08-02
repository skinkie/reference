from dataclasses import dataclass, field
from typing import List, Optional, Union

from .abstract_monitored_call_structure import AbstractMonitoredCallStructure
from .actual_arrival_time import ActualArrivalTime
from .actual_departure_time import ActualDepartureTime
from .aimed_arrival_time import AimedArrivalTime
from .aimed_departure_time import AimedDepartureTime
from .expected_arrival_time import ExpectedArrivalTime
from .expected_departure_time import ExpectedDepartureTime
from .extensions_1 import Extensions1
from .recorded_departure_capacities import RecordedDepartureCapacities
from .recorded_departure_occupancy import RecordedDepartureOccupancy
from .vehicle_at_stop import VehicleAtStop

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class PreviousCallStructure(AbstractMonitoredCallStructure):
    vehicle_at_stop: Optional[VehicleAtStop] = field(
        default=None,
        metadata={
            "name": "VehicleAtStop",
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
    recorded_departure_occupancy: List[RecordedDepartureOccupancy] = field(
        default_factory=list,
        metadata={
            "name": "RecordedDepartureOccupancy",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    recorded_departure_capacities: List[RecordedDepartureCapacities] = field(
        default_factory=list,
        metadata={
            "name": "RecordedDepartureCapacities",
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
