from dataclasses import dataclass
from .customer_purchase_package_price_ref_structure import (
    CustomerPurchasePackagePriceRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerPurchasePackagePriceRef(
    CustomerPurchasePackagePriceRefStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
