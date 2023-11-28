from dataclasses import dataclass, field
from typing import List
from netex.fulfilment_method_ref import FulfilmentMethodRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FulfilmentMethodRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a collection of one or more references to a FULFILMENT METHOD.
    """
    class Meta:
        name = "fulfilmentMethodRefs_RelStructure"

    fulfilment_method_ref: List[FulfilmentMethodRef] = field(
        default_factory=list,
        metadata={
            "name": "FulfilmentMethodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
