from dataclasses import dataclass

from .journey_designator_structure import JourneyDesignatorStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class JourneyDesignator(JourneyDesignatorStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
