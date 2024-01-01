from dataclasses import dataclass
from .journey_pattern_run_time_ref_structure import (
    JourneyPatternRunTimeRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyPatternRunTimeRef(JourneyPatternRunTimeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
