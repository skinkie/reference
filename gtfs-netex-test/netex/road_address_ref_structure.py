from dataclasses import dataclass

from .address_ref_structure import AddressRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class RoadAddressRefStructure(AddressRefStructure):
    pass
