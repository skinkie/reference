from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .type_of_sales_offer_package_ref import TypeOfSalesOfferPackageRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfsalesOfferPackageRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "typeOfsalesOfferPackageRefs_RelStructure"

    type_of_sales_offer_package_ref: list[TypeOfSalesOfferPackageRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfSalesOfferPackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
