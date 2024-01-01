from dataclasses import dataclass
from .timing_pattern_version_structure import TimingPatternVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimingPattern(TimingPatternVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
