from dataclasses import dataclass
from .customer_version_structure import CustomerVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Customer(CustomerVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
