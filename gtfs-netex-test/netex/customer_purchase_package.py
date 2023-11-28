from dataclasses import dataclass, field
from netex.customer_purchase_package_version_structure import CustomerPurchasePackageVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomerPurchasePackage(CustomerPurchasePackageVersionStructure):
    """
    A purchase of a SALES OFFER PACKAGE by a CUSTOMER, giving access rights to one
    or several FARE PRODUCTs materialised as one or several TRAVEL DOCUMENTs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
