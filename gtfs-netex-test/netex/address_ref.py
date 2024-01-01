from dataclasses import dataclass
from .address_ref_structure import AddressRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AddressRef(AddressRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
