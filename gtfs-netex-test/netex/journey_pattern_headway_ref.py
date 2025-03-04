from dataclasses import dataclass

from .journey_pattern_run_time_ref_structure import JourneyPatternRunTimeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class JourneyPatternHeadwayRef(JourneyPatternRunTimeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
