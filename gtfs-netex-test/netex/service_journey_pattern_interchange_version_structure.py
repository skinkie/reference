from dataclasses import dataclass, field
from typing import Optional
from netex.interchange_version_structure import InterchangeVersionStructure
from netex.journey_pattern_ref_structure import JourneyPatternRefStructure
from netex.scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceJourneyPatternInterchangeVersionStructure(InterchangeVersionStructure):
    """
    Type for SERVICE JOURNEY PATTERN INTERCHANGE.

    :ivar from_point_ref: SCHEDULED STOP POINT feeding INTERCHANGE.
    :ivar from_visit_number: Visit number to distinguish which visit to
        FROM SCHEDULED STOP POINT this is. Default is one. Only needed
        for circular routes with connections at the same stop on
        different visits.
    :ivar to_point_ref: SCHEDULED STOP POINT distributing from
        INTERCHANGE.
    :ivar to_visit_number: Visit number to distinguish which visit to TO
        SCHEDULED STOP POINT  this is. Default is one. Only needed for
        circular routes with connections at the same stop on different
        visits.
    :ivar from_journey_pattern_ref: JOURNEY PATTERN that feeds
        INTERCHANGE.
    :ivar to_journey_pattern_ref: JOURNEY PATTERN that distributes from
        INTERCHANGE.
    """
    class Meta:
        name = "ServiceJourneyPatternInterchange_VersionStructure"

    from_point_ref: ScheduledStopPointRefStructure = field(
        metadata={
            "name": "FromPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    from_visit_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "FromVisitNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    to_point_ref: ScheduledStopPointRefStructure = field(
        metadata={
            "name": "ToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    to_visit_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "ToVisitNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    from_journey_pattern_ref: JourneyPatternRefStructure = field(
        metadata={
            "name": "FromJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    to_journey_pattern_ref: JourneyPatternRefStructure = field(
        metadata={
            "name": "ToJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
