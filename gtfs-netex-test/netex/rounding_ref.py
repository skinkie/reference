from dataclasses import dataclass
from .rounding_ref_structure import RoundingRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoundingRef(RoundingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
