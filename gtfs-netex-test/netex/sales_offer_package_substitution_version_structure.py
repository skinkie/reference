from dataclasses import dataclass, field
from typing import Optional
from netex.assignment_version_structure_1 import AssignmentVersionStructure1
from netex.sales_offer_package_ref import SalesOfferPackageRef
from netex.sales_offer_package_ref_structure import SalesOfferPackageRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SalesOfferPackageSubstitutionVersionStructure(AssignmentVersionStructure1):
    """
    Type for SALES OFFER PACKAGE SUBSTITUTION.

    :ivar sales_offer_package_ref:
    :ivar with_sales_offer_package_ref: SALES OFFER PACKAGE  that may be
        used to subsitute base SALES OFFER PACKAGE.
    """
    class Meta:
        name = "SalesOfferPackageSubstitution_VersionStructure"

    sales_offer_package_ref: Optional[SalesOfferPackageRef] = field(
        default=None,
        metadata={
            "name": "SalesOfferPackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    with_sales_offer_package_ref: SalesOfferPackageRefStructure = field(
        metadata={
            "name": "WithSalesOfferPackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
