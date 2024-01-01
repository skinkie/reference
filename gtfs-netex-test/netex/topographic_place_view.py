from dataclasses import dataclass
from .topographic_place_derived_view_structure import (
    TopographicPlaceDerivedViewStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TopographicPlaceView(TopographicPlaceDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
