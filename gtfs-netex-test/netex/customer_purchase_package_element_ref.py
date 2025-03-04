from dataclasses import dataclass

from .customer_purchase_package_element_ref_structure import CustomerPurchasePackageElementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CustomerPurchasePackageElementRef(CustomerPurchasePackageElementRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
