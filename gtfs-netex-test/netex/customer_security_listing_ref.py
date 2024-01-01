from dataclasses import dataclass
from .customer_security_listing_ref_structure import (
    CustomerSecurityListingRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerSecurityListingRef(CustomerSecurityListingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
