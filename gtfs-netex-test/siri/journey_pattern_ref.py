from dataclasses import dataclass

from .journey_pattern_ref_structure import JourneyPatternRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class JourneyPatternRef(JourneyPatternRefStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
