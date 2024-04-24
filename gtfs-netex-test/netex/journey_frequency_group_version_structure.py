from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional, Union

from xsdata.models.datatype import XmlTime

from .explicit_journey_refs_rel_structure import ExplicitJourneyRefsRelStructure
from .group_of_entities_version_structure import GroupOfEntitiesVersionStructure
from .time_demand_type_refs_rel_structure import TimeDemandTypeRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyFrequencyGroupVersionStructure(GroupOfEntitiesVersionStructure):
    class Meta:
        name = "JourneyFrequencyGroup_VersionStructure"

    first_departure_time: XmlTime = field(
        metadata={
            "name": "FirstDepartureTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    first_day_offset_or_last_departure_time_or_last_day_offset_or_first_arrival_time_or_last_arrival_time: List[
        Union["JourneyFrequencyGroupVersionStructure.FirstDayOffset", "JourneyFrequencyGroupVersionStructure.LastDepartureTime", "JourneyFrequencyGroupVersionStructure.LastDayOffset", "JourneyFrequencyGroupVersionStructure.FirstArrivalTime", "JourneyFrequencyGroupVersionStructure.LastArrivalTime"]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FirstDayOffset",
                    "type": ForwardRef("JourneyFrequencyGroupVersionStructure.FirstDayOffset"),
                    "namespace": "http://www.netex.org.uk/netex",
                    "max_occurs": 2,
                },
                {
                    "name": "LastDepartureTime",
                    "type": ForwardRef("JourneyFrequencyGroupVersionStructure.LastDepartureTime"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LastDayOffset",
                    "type": ForwardRef("JourneyFrequencyGroupVersionStructure.LastDayOffset"),
                    "namespace": "http://www.netex.org.uk/netex",
                    "max_occurs": 2,
                },
                {
                    "name": "FirstArrivalTime",
                    "type": ForwardRef("JourneyFrequencyGroupVersionStructure.FirstArrivalTime"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LastArrivalTime",
                    "type": ForwardRef("JourneyFrequencyGroupVersionStructure.LastArrivalTime"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 5,
        },
    )
    time_demand_types: Optional[TimeDemandTypeRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "timeDemandTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journeys: Optional[ExplicitJourneyRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )

    @dataclass(kw_only=True)
    class FirstDayOffset:
        value: int = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class LastDepartureTime:
        value: XmlTime = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class LastDayOffset:
        value: int = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class FirstArrivalTime:
        value: XmlTime = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class LastArrivalTime:
        value: XmlTime = field(
            metadata={
                "required": True,
            }
        )
