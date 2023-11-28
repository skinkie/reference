from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.dead_run_ref import DeadRunRef
from netex.journey_timing_versioned_child_structure import JourneyTimingVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DefaultDeadRunRunTimeVersionedChildStructure(JourneyTimingVersionedChildStructure):
    """
    Type for DEFAULT DEAD RUN / RUN TIME.

    :ivar run_time: Run time as interval.
    :ivar dead_run_ref:
    """
    class Meta:
        name = "DefaultDeadRunRunTime_VersionedChildStructure"

    run_time: XmlDuration = field(
        metadata={
            "name": "RunTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    dead_run_ref: Optional[DeadRunRef] = field(
        default=None,
        metadata={
            "name": "DeadRunRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
