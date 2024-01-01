from dataclasses import dataclass
from .topographic_place_ref_structure import TopographicPlaceRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TopographicPlaceRef(TopographicPlaceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
