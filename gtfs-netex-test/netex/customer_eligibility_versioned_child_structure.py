from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_texts_rel_structure import VersionedChildStructure
from netex.customer_ref import CustomerRef
from netex.multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomerEligibilityVersionedChildStructure(VersionedChildStructure):
    """
    Type for CUSTOMER ELIGIBILITY.

    :ivar name: Name of CUSTOMER ELIGIBILITY.
    :ivar customer_ref:
    """
    class Meta:
        name = "CustomerEligibility_VersionedChildStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_ref: Optional[CustomerRef] = field(
        default=None,
        metadata={
            "name": "CustomerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
