from dataclasses import dataclass, field
from typing import Optional
from .interchange_version_structure import InterchangeVersionStructure
from .journey_pattern_ref_structure import JourneyPatternRefStructure
from .scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceJourneyPatternInterchangeVersionStructure(
    InterchangeVersionStructure
):
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
        },
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
        },
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
