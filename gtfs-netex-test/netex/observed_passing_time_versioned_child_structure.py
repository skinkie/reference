from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional, Union

from xsdata.models.datatype import XmlDuration, XmlTime

from .dated_passing_time_versioned_child_structure import DatedPassingTimeVersionedChildStructure
from .headway_interval_structure import HeadwayIntervalStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ObservedPassingTimeVersionedChildStructure(DatedPassingTimeVersionedChildStructure):
    class Meta:
        name = "ObservedPassingTime_VersionedChildStructure"

    actual_arrival_time_or_arrival_day_offset_or_actual_departure_time_or_departure_day_offset_or_actual_waiting_time_or_actual_nonstop_passing_time_or_passing_time_day_offset: List[
        Union[
            "ObservedPassingTimeVersionedChildStructure.ActualArrivalTime",
            "ObservedPassingTimeVersionedChildStructure.ArrivalDayOffset",
            "ObservedPassingTimeVersionedChildStructure.ActualDepartureTime",
            "ObservedPassingTimeVersionedChildStructure.DepartureDayOffset",
            XmlDuration,
            "ObservedPassingTimeVersionedChildStructure.ActualNonstopPassingTime",
            "ObservedPassingTimeVersionedChildStructure.PassingTimeDayOffset",
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ActualArrivalTime",
                    "type": ForwardRef("ObservedPassingTimeVersionedChildStructure.ActualArrivalTime"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ArrivalDayOffset",
                    "type": ForwardRef("ObservedPassingTimeVersionedChildStructure.ArrivalDayOffset"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActualDepartureTime",
                    "type": ForwardRef("ObservedPassingTimeVersionedChildStructure.ActualDepartureTime"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DepartureDayOffset",
                    "type": ForwardRef("ObservedPassingTimeVersionedChildStructure.DepartureDayOffset"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActualWaitingTime",
                    "type": XmlDuration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActualNonstopPassingTime",
                    "type": ForwardRef("ObservedPassingTimeVersionedChildStructure.ActualNonstopPassingTime"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassingTimeDayOffset",
                    "type": ForwardRef("ObservedPassingTimeVersionedChildStructure.PassingTimeDayOffset"),
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
