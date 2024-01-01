from dataclasses import dataclass
from .stop_place_derived_view_structure import StopPlaceDerivedViewStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopPlaceView(StopPlaceDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    branding_ref: RestrictedVar
