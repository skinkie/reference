from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.journey_timing_versioned_child_structure import JourneyTimingVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TurnaroundTimeLimitTimeVersionedChildStructure(JourneyTimingVersionedChildStructure):
    """
    Type for TURNAROUND TIME LIMIT.

    :ivar minimum_duration: Minimum turnaround time as an interval.
    :ivar maximum_duration: Maximum turnaround time as an interval.
    """
    class Meta:
        name = "TurnaroundTimeLimitTime_VersionedChildStructure"

    minimum_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
