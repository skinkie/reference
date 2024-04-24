from dataclasses import dataclass

from .locatable_spot_version_structure import LocatableSpotVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LocatableSpot(LocatableSpotVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
