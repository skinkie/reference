from dataclasses import dataclass

from .locatable_spot_ref_structure import LocatableSpotRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LocatableSpotRef(LocatableSpotRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
