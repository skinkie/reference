from dataclasses import dataclass

from .group_of_customer_purchase_packages_ref_structure import GroupOfCustomerPurchasePackagesRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class GroupOfCustomerPurchasePackagesRef(GroupOfCustomerPurchasePackagesRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
