from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.journey_timing_versioned_child_structure import JourneyTimingVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyHeadwayVersionedChildStructure(JourneyTimingVersionedChildStructure):
    """
    Type for a JOURNEY HEADWAY Interval.

    :ivar scheduled_headway_interval: Scheduled normal headway interval.
    :ivar minimum_headway_interval: Minimum headway interval.
    :ivar maximum_headway_interval: Maximum headway interval.
    """
    class Meta:
        name = "JourneyHeadway_VersionedChildStructure"

    scheduled_headway_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ScheduledHeadwayInterval",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    minimum_headway_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumHeadwayInterval",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_headway_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumHeadwayInterval",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
