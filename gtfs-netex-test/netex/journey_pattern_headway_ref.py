from dataclasses import dataclass
from netex.journey_pattern_run_time_ref_structure import JourneyPatternRunTimeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyPatternHeadwayRef(JourneyPatternRunTimeRefStructure):
    """
    Reference to a JOURNEY PATTERN HEADWAY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
