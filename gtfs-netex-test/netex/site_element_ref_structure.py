from dataclasses import dataclass
from .addressable_place_ref_structure import AddressablePlaceRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteElementRefStructure(AddressablePlaceRefStructure):
    value: RestrictedVar
