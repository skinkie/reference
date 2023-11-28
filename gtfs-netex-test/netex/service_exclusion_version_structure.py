from dataclasses import dataclass, field
from typing import Optional
from netex.assignment_version_structure_1 import AssignmentVersionStructure1
from netex.journey_pattern_ref_structure import JourneyPatternRefStructure
from netex.journey_pattern_refs_rel_structure import JourneyPatternRefsRelStructure
from netex.scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceExclusionVersionStructure(AssignmentVersionStructure1):
    """
    Type for SERVICE EXCLUSION.

    :ivar excluding_journey_pattern_ref: JOURNEY PATTERN to which
        exclusion applies.
    :ivar start_point_ref: Starting stop point within JOURNEY PATTERN
        for exclusion.
    :ivar end_point_ref: Ending stop point within JOURNEY PATTERN for
        exclusion.
    :ivar excluded_journey_pattern_refs: Excluded other JOIURNEY
        PATTERNs.
    """
    class Meta:
        name = "ServiceExclusion_VersionStructure"

    excluding_journey_pattern_ref: Optional[JourneyPatternRefStructure] = field(
        default=None,
        metadata={
            "name": "ExcludingJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_point_ref: Optional[ScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "StartPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_point_ref: Optional[ScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "EndPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    excluded_journey_pattern_refs: Optional[JourneyPatternRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "excludedJourneyPatternRefs",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
