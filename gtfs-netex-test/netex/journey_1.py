from dataclasses import dataclass

from .journey_version_structure import JourneyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class Journey1(JourneyVersionStructure):
    class Meta:
        name = "Journey"
        namespace = "http://www.netex.org.uk/netex"
