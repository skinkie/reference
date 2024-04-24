from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional, Union

from xsdata.models.datatype import XmlDuration, XmlTime

from .headway_interval_structure import HeadwayIntervalStructure
from .passing_time_view_structure import PassingTimeViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EstimatedPassingTimeViewStructure(PassingTimeViewStructure):
    class Meta:
        name = "EstimatedPassingTime_ViewStructure"

    expected_arrival_time_or_arrival_day_offset_or_expected_departure_time_or_departure_day_offset_or_expected_waiting_time_or_expected_nonstop_passing_time_or_passing_time_day_offset: List[
        Union[
            "EstimatedPassingTimeViewStructure.ExpectedArrivalTime",
            "EstimatedPassingTimeViewStructure.ArrivalDayOffset",
            "EstimatedPassingTimeViewStructure.ExpectedDepartureTime",
            "EstimatedPassingTimeViewStructure.DepartureDayOffset",
            XmlDuration,
            "EstimatedPassingTimeViewStructure.ExpectedNonstopPassingTime",
            "EstimatedPassingTimeViewStructure.PassingTimeDayOffset",
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ExpectedArrivalTime",
                    "type": ForwardRef("EstimatedPassingTimeViewStructure.ExpectedArrivalTime"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ArrivalDayOffset",
                    "type": ForwardRef("EstimatedPassingTimeViewStructure.ArrivalDayOffset"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ExpectedDepartureTime",
                    "type": ForwardRef("EstimatedPassingTimeViewStructure.ExpectedDepartureTime"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DepartureDayOffset",
                    "type": ForwardRef("EstimatedPassingTimeViewStructure.DepartureDayOffset"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ExpectedWaitingTime",
                    "type": XmlDuration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ExpectedNonstopPassingTime",
                    "type": ForwardRef("EstimatedPassingTimeViewStructure.ExpectedNonstopPassingTime"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassingTimeDayOffset",
                    "type": ForwardRef("EstimatedPassingTimeViewStructure.PassingTimeDayOffset"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 5,
        },
    )
    expected_headway: Optional[HeadwayIntervalStructure] = field(
        default=None,
        metadata={
            "name": "ExpectedHeadway",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )

    @dataclass(kw_only=True)
    class ExpectedArrivalTime:
        value: XmlTime = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ArrivalDayOffset:
        value: int = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ExpectedDepartureTime:
        value: XmlTime = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class DepartureDayOffset:
        value: int = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ExpectedNonstopPassingTime:
        value: XmlTime = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class PassingTimeDayOffset:
        value: int = field(
            metadata={
                "required": True,
            }
        )
