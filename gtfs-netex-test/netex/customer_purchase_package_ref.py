from dataclasses import dataclass
from .customer_purchase_package_ref_structure import (
    CustomerPurchasePackageRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerPurchasePackageRef(CustomerPurchasePackageRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
