from dataclasses import dataclass, field
from netex.customer_purchase_package_element_version_structure import CustomerPurchasePackageElementVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomerPurchasePackageElement(CustomerPurchasePackageElementVersionStructure):
    """
    The assignment of a  SALES OFFER PACKAGE ELEMENT, for use in a CUSTOMER SALES
    PACKAGE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
