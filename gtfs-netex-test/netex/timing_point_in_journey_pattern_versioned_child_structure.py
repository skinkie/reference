from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.border_point_ref import BorderPointRef
from netex.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from netex.garage_point_ref import GaragePointRef
from netex.journey_pattern_headways_rel_structure import JourneyPatternHeadwaysRelStructure
from netex.journey_pattern_wait_times_rel_structure import JourneyPatternWaitTimesRelStructure
from netex.notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from netex.parking_point_ref import ParkingPointRef
from netex.point_in_link_sequence_versioned_child_structure import PointInLinkSequenceVersionedChildStructure
from netex.relief_point_ref import ReliefPointRef
from netex.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.timing_link_ref_structure import TimingLinkRefStructure
from netex.timing_point_ref import TimingPointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimingPointInJourneyPatternVersionedChildStructure(PointInLinkSequenceVersionedChildStructure):
    """
    Type for TIMING POINT IN JOURNEY PATTERN.

    :ivar choice_1:
    :ivar onward_timing_link_ref: Used to disambiguate if multiple links
        between the same points.
    :ivar is_wait_point: Whether point is a wait point.
    :ivar wait_time_or_wait_times:
    :ivar headways: Wait times for TIMING POINT. There may be different
        times for different time demands.
    :ivar notice_assignments: NOTICEs for TIMING POINT IN JOURNEY
        PATTERN.
    """
    class Meta:
        name = "TimingPointInJourneyPattern_VersionedChildStructure"

    choice_1: Optional[object] = field(
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
    onward_timing_link_ref: Optional[TimingLinkRefStructure] = field(
        default=None,
        metadata={
            "name": "OnwardTimingLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    is_wait_point: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsWaitPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wait_time_or_wait_times: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "WaitTime",
                    "type": XmlDuration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "waitTimes",
                    "type": JourneyPatternWaitTimesRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    headways: Optional[JourneyPatternHeadwaysRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notice_assignments: Optional[NoticeAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
