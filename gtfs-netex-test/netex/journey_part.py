from dataclasses import dataclass
from .journey_part_version_structure import JourneyPartVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyPart(JourneyPartVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
