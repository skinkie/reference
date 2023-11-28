from dataclasses import dataclass
from netex.target_passing_time_ref_structure import TargetPassingTimeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TargetPassingTimeRef(TargetPassingTimeRefStructure):
    """
    Reference to a TARGET PASSING TIME.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
