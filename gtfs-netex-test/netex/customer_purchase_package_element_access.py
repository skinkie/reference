from dataclasses import dataclass
from .customer_purchase_package_element_access_versioned_child_structure import (
    CustomerPurchasePackageElementAccessVersionedChildStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerPurchasePackageElementAccess(
    CustomerPurchasePackageElementAccessVersionedChildStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions: RestrictedVar
    valid_between: RestrictedVar
    alternative_texts: RestrictedVar
