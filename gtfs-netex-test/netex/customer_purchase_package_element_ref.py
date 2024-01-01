from dataclasses import dataclass
from .customer_purchase_package_element_ref_structure import (
    CustomerPurchasePackageElementRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerPurchasePackageElementRef(
    CustomerPurchasePackageElementRefStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
