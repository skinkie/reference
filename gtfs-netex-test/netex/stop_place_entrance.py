from dataclasses import dataclass
from .stop_place_entrance_version_structure import (
    StopPlaceEntranceVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopPlaceEntrance(StopPlaceEntranceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    members: RestrictedVar
