from dataclasses import dataclass
from .fare_point_in_pattern_ref_structure import FarePointInPatternRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FarePointInPatternRef(FarePointInPatternRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
