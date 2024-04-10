from dataclasses import dataclass

from .journey_pattern_derived_view_structure import JourneyPatternDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyPatternView(JourneyPatternDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
