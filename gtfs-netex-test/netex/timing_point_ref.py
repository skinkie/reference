from dataclasses import dataclass
from netex.timing_point_ref_structure import TimingPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimingPointRef(TimingPointRefStructure):
    """Reference to a TIMING POINT.

    If given by context does not need to be stated.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
