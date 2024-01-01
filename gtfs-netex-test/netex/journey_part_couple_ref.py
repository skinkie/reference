from dataclasses import dataclass
from .journey_part_couple_ref_structure import JourneyPartCoupleRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyPartCoupleRef(JourneyPartCoupleRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
