from dataclasses import dataclass
from netex.timing_pattern_ref_structure import TimingPatternRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimingPatternRef(TimingPatternRefStructure):
    """
    Reference to a TIMING PATTERN.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
