from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDuration, XmlTime
from netex.headway_interval_structure import HeadwayIntervalStructure
from netex.passing_time_view_structure import PassingTimeViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class EstimatedPassingTimeViewStructure(PassingTimeViewStructure):
    """
    Type for Simplified  ESTIMATED PASSING TIME.

    :ivar choice:
    :ivar expected_headway: Expected Frequency of service.
    """
    class Meta:
        name = "EstimatedPassingTime_ViewStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ExpectedArrivalTime",
                    "type": XmlTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ArrivalDayOffset",
                    "type": int,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ExpectedDepartureTime",
                    "type": XmlTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DepartureDayOffset",
                    "type": int,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ExpectedWaitingTime",
                    "type": XmlDuration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ExpectedNonstopPassingTime",
                    "type": XmlTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassingTimeDayOffset",
                    "type": int,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 5,
        }
    )
    expected_headway: Optional[HeadwayIntervalStructure] = field(
        default=None,
        metadata={
            "name": "ExpectedHeadway",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
