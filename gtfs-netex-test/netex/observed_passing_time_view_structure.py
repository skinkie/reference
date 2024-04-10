from dataclasses import dataclass, field
from typing import List, Optional, Type, Union

from xsdata.models.datatype import XmlDuration, XmlTime

from .headway_interval_structure import HeadwayIntervalStructure
from .passing_time_view_structure import PassingTimeViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ObservedPassingTimeViewStructure(PassingTimeViewStructure):
    class Meta:
        name = "ObservedPassingTime_ViewStructure"

    actual_arrival_time_or_arrival_day_offset_or_actual_departure_time_or_departure_day_offset_or_actual_waiting_time_or_actual_nonstop_passing_time_or_passing_time_day_offset: List[
        Union[
            "ObservedPassingTimeViewStructure.ActualArrivalTime",
            "ObservedPassingTimeViewStructure.ArrivalDayOffset",
            "ObservedPassingTimeViewStructure.ActualDepartureTime",
            "ObservedPassingTimeViewStructure.DepartureDayOffset",
            XmlDuration,
            "ObservedPassingTimeViewStructure.ActualNonstopPassingTime",
            "ObservedPassingTimeViewStructure.PassingTimeDayOffset",
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ActualArrivalTime",
                    "type": Type["ObservedPassingTimeViewStructure.ActualArrivalTime"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ArrivalDayOffset",
                    "type": Type["ObservedPassingTimeViewStructure.ArrivalDayOffset"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActualDepartureTime",
                    "type": Type["ObservedPassingTimeViewStructure.ActualDepartureTime"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DepartureDayOffset",
                    "type": Type["ObservedPassingTimeViewStructure.DepartureDayOffset"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActualWaitingTime",
                    "type": XmlDuration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActualNonstopPassingTime",
                    "type": Type["ObservedPassingTimeViewStructure.ActualNonstopPassingTime"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassingTimeDayOffset",
                    "type": Type["ObservedPassingTimeViewStructure.PassingTimeDayOffset"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 5,
        },
    )
    actual_headway: Optional[HeadwayIntervalStructure] = field(
        default=None,
        metadata={
            "name": "ActualHeadway",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )

    @dataclass(kw_only=True)
    class ActualArrivalTime:
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
    class ActualDepartureTime:
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
    class ActualNonstopPassingTime:
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
