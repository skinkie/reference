from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlTime
from netex.alternative_texts_rel_structure import VersionedChildStructure
from netex.fare_demand_factor_ref import FareDemandFactorRef
from netex.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from netex.scheduled_stop_point_ref import ScheduledStopPointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StartTimeAtStopPointVersionedChildStructure(VersionedChildStructure):
    """
    Type for START TIME AT STOP POINT.

    :ivar fare_demand_factor_ref:
    :ivar fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref:
    :ivar start_time: Time at stop at which FARE DEMAND PERIOD starts.
    :ivar end_time: Time at stop at whichARE DEMAND PERIODends.
    :ivar day_offset: Day Offset for end time from start time. 0= same
        day.
    """
    class Meta:
        name = "StartTimeAtStopPoint_VersionedChildStructure"

    fare_demand_factor_ref: Optional[FareDemandFactorRef] = field(
        default=None,
        metadata={
            "name": "FareDemandFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareScheduledStopPointRef",
                    "type": FareScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledStopPointRef",
                    "type": ScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    start_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "DayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
