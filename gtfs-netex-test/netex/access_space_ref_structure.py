from dataclasses import dataclass
from .stop_place_space_ref_structure import StopPlaceSpaceRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessSpaceRefStructure(StopPlaceSpaceRefStructure):
    value: RestrictedVar
