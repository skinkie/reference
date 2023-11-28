from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.type_of_fare_product_ref import TypeOfFareProductRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfFareProductRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of TYPEs OF FARE PRODUCT.
    """
    class Meta:
        name = "typeOfFareProductRefs_RelStructure"

    type_of_fare_product_ref: List[TypeOfFareProductRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
