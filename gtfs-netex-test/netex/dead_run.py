from dataclasses import dataclass, field
from netex.dead_run_with_calls_version_structure import DeadRunWithCallsVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DeadRun(DeadRunWithCallsVersionStructure):
    """
    A non-service VEHICLE JOURNEY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
