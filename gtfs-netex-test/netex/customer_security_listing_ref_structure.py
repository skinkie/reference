from dataclasses import dataclass
from .security_listing_ref_structure import SecurityListingRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerSecurityListingRefStructure(SecurityListingRefStructure):
    value: RestrictedVar
