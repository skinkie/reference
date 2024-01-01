from dataclasses import dataclass
from .flexible_stop_place_version_structure import (
    FlexibleStopPlaceVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleStopPlace(FlexibleStopPlaceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
