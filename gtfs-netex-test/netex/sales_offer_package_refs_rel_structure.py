from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.sales_offer_package_ref import SalesOfferPackageRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SalesOfferPackageRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a collection of one or more references to a SALES OFFER PACKAGE.
    """
    class Meta:
        name = "salesOfferPackageRefs_RelStructure"

    sales_offer_package_ref: List[SalesOfferPackageRef] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
