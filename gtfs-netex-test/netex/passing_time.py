from dataclasses import dataclass
from netex.passing_time_versioned_child_structure import PassingTimeVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PassingTime(PassingTimeVersionedChildStructure):
    """
    PASSING TIME.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
