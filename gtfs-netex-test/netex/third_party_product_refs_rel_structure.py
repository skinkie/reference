from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .third_party_product_ref import ThirdPartyProductRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ThirdPartyProductRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "thirdPartyProductRefs_RelStructure"

    third_party_product_ref: list[ThirdPartyProductRef] = field(
        default_factory=list,
        metadata={
            "name": "ThirdPartyProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
