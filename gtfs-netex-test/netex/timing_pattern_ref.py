from dataclasses import dataclass
from .timing_pattern_ref_structure import TimingPatternRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimingPatternRef(TimingPatternRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
