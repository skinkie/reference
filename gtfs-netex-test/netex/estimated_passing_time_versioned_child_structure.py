from dataclasses import dataclass, field
from typing import List, Optional, Type, Union

from xsdata.models.datatype import XmlDuration, XmlTime

from .dated_passing_time_versioned_child_structure import DatedPassingTimeVersionedChildStructure
from .headway_interval_structure import HeadwayIntervalStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EstimatedPassingTimeVersionedChildStructure(DatedPassingTimeVersionedChildStructure):
    class Meta:
        name = "EstimatedPassingTime_VersionedChildStructure"

    expected_arrival_time_or_arrival_day_offset_or_expected_departure_time_or_departure_day_offset_or_expected_waiting_time_or_expected_nonstop_passing_time_or_passing_time_day_offset: List[
        Union[
            "EstimatedPassingTimeVersionedChildStructure.ExpectedArrivalTime",
            "EstimatedPassingTimeVersionedChildStructure.ArrivalDayOffset",
            "EstimatedPassingTimeVersionedChildStructure.ExpectedDepartureTime",
            "EstimatedPassingTimeVersionedChildStructure.DepartureDayOffset",
            XmlDuration,
            "EstimatedPassingTimeVersionedChildStructure.ExpectedNonstopPassingTime",
            "EstimatedPassingTimeVersionedChildStructure.PassingTimeDayOffset",
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ExpectedArrivalTime",
                    "type": Type["EstimatedPassingTimeVersionedChildStructure.ExpectedArrivalTime"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ArrivalDayOffset",
                    "type": Type["EstimatedPassingTimeVersionedChildStructure.ArrivalDayOffset"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ExpectedDepartureTime",
                    "type": Type["EstimatedPassingTimeVersionedChildStructure.ExpectedDepartureTime"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DepartureDayOffset",
                    "type": Type["EstimatedPassingTimeVersionedChildStructure.DepartureDayOffset"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ExpectedWaitingTime",
                    "type": XmlDuration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ExpectedNonstopPassingTime",
                    "type": Type["EstimatedPassingTimeVersionedChildStructure.ExpectedNonstopPassingTime"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassingTimeDayOffset",
                    "type": Type["EstimatedPassingTimeVersionedChildStructure.PassingTimeDayOffset"],
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
