from dataclasses import dataclass

from .journey_pattern_run_time_versioned_child_structure import JourneyPatternRunTimeVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class JourneyPatternRunTime(JourneyPatternRunTimeVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
