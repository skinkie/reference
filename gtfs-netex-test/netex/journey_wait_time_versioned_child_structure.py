from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.border_point_ref import BorderPointRef
from netex.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from netex.garage_point_ref import GaragePointRef
from netex.journey_timing_versioned_child_structure import JourneyTimingVersionedChildStructure
from netex.parking_point_ref import ParkingPointRef
from netex.relief_point_ref import ReliefPointRef
from netex.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.timing_point_ref import TimingPointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyWaitTimeVersionedChildStructure(JourneyTimingVersionedChildStructure):
    """
    Type for JOURNEY WAIT TIME.

    :ivar choice:
    :ivar wait_time: Wait time as interval.
    """
    class Meta:
        name = "JourneyWaitTime_VersionedChildStructure"

    choice: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "BorderPointRef",
                    "type": BorderPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "GaragePointRef",
                    "type": GaragePointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPointRef",
                    "type": ParkingPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReliefPointRef",
                    "type": ReliefPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingPointRef",
                    "type": TimingPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    wait_time: XmlDuration = field(
        metadata={
            "name": "WaitTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
