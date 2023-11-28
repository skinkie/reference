from dataclasses import dataclass
from netex.dead_run_ref_structure import DeadRunRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DeadRunRef(DeadRunRefStructure):
    """
    Reference to a DEAD RUN.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
