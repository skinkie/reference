from dataclasses import dataclass

from .timing_pattern_ref_structure import TimingPatternRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TimingPatternRef(TimingPatternRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
