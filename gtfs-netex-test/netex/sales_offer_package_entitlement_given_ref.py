from dataclasses import dataclass
from .sales_offer_package_entitlement_given_ref_structure import (
    SalesOfferPackageEntitlementGivenRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SalesOfferPackageEntitlementGivenRef(
    SalesOfferPackageEntitlementGivenRefStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
