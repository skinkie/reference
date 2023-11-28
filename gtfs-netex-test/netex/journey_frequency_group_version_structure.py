from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlTime
from netex.explicit_journey_refs_rel_structure import ExplicitJourneyRefsRelStructure
from netex.group_of_entities_version_structure import GroupOfEntitiesVersionStructure
from netex.time_demand_type_refs_rel_structure import TimeDemandTypeRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyFrequencyGroupVersionStructure(GroupOfEntitiesVersionStructure):
    """
    Type for   JOURNEY FREQUENCY GROUP.

    :ivar first_departure_time: Time of first departure in JOURNEY
        FREQUENCY GROUP.
    :ivar first_day_offset: Offset days for end time. Number of days
        after the starting operational day if journey if  not same
        calendar day. Default is 0 for same day.
    :ivar last_departure_time: Time of last departure in JOURNEY
        FREQUENCY GROUP.
    :ivar last_day_offset: Offset days for end time. Number of days
        after the starting departure time of the journey if  not same
        calendar day. Default is 0 for same day.
    :ivar time_demand_types: TIME DEMAND TYPES associated with JOURNEY
        FREQUENCY GROUP.
    :ivar journeys: TIME DEMAND TYPES associated with JOURNEY FREQUENCY
        GROUP.
    """
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
    first_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "FirstDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    last_departure_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "LastDepartureTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    last_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "LastDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_demand_types: Optional[TimeDemandTypeRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "timeDemandTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journeys: Optional[ExplicitJourneyRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
