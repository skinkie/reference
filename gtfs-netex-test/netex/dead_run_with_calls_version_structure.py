from dataclasses import dataclass, field
from typing import Optional
from netex.dead_run_calls_rel_structure import DeadRunCallsRelStructure
from netex.dead_run_version_structure import DeadRunVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DeadRunWithCallsVersionStructure(DeadRunVersionStructure):
    """
    Type for  DEAD RUN.

    :ivar calls: Complete sequence of stops along the route path, in
        calling order.
    """
    class Meta:
        name = "DeadRunWithCalls_VersionStructure"

    calls: Optional[DeadRunCallsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
