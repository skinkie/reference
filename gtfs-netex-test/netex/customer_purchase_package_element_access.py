from dataclasses import dataclass, field
from netex.customer_purchase_package_element_access_versioned_child_structure import CustomerPurchasePackageElementAccessVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomerPurchasePackageElementAccess(CustomerPurchasePackageElementAccessVersionedChildStructure):
    """Access to a VALIDABLE ELEMENT by a specific CUSTOMER PURCHASE PACKAGE
    through use of CUSTOMER PURCHASE PACKAGE.

    This is needed for validation of complex SALES OFFER PACKAGEs
    containing tariffs structures that have FARE STRUCTURE ELEMENTs IN
    SEQUENCE, in such a case a given SALES PACKAGE ELEMENT may have
    multiple VALIDABLE ELEMENTs associated with it, each of which can be
    separately validated and marked. +v1.1
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
