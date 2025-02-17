from dataclasses import dataclass, field
from typing import Optional, Union

from .assignment_version_structure_1 import AssignmentVersionStructure1
from .flexible_line_ref import FlexibleLineRef
from .journey_pattern_ref_structure import JourneyPatternRefStructure
from .journey_pattern_refs_rel_structure import JourneyPatternRefsRelStructure
from .line_ref import LineRef
from .scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ServiceExclusionVersionStructure(AssignmentVersionStructure1):
    class Meta:
        name = "ServiceExclusion_VersionStructure"

    excluding_journey_pattern_ref: Optional[JourneyPatternRefStructure] = field(
        default=None,
        metadata={
            "name": "ExcludingJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    start_point_ref: Optional[ScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "StartPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_point_ref: Optional[ScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "EndPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    excluded_journey_pattern_refs: Optional[JourneyPatternRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "excludedJourneyPatternRefs",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    line_ref: Optional[Union[FlexibleLineRef, LineRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleLineRef",
                    "type": FlexibleLineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineRef",
                    "type": LineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
