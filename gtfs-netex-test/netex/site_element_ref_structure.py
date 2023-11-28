from dataclasses import dataclass
from netex.addressable_place_ref_structure import AddressablePlaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SiteElementRefStructure(AddressablePlaceRefStructure):
    """
    Type for reference to a SITE COMPONENT.
    """
