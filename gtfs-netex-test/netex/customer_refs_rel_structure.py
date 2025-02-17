from dataclasses import dataclass, field

from .customer_ref import CustomerRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CustomerRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "customerRefs_RelStructure"

    customer_ref: list[CustomerRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
