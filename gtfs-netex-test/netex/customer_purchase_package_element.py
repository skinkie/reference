from dataclasses import dataclass
from .customer_purchase_package_element_version_structure import (
    CustomerPurchasePackageElementVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerPurchasePackageElement(
    CustomerPurchasePackageElementVersionStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
