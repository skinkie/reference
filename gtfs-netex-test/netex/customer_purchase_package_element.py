from dataclasses import dataclass

from .customer_purchase_package_element_version_structure import CustomerPurchasePackageElementVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CustomerPurchasePackageElement(CustomerPurchasePackageElementVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
