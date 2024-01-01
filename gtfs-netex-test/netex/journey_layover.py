from dataclasses import dataclass
from .journey_layover_structure import JourneyLayoverStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyLayover(JourneyLayoverStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
