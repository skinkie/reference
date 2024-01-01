from dataclasses import dataclass
from .stop_place_ref_structure import StopPlaceRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TaxiRankRefStructure(StopPlaceRefStructure):
    value: RestrictedVar
