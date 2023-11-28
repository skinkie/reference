from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.type_of_payment_method_ref import TypeOfPaymentMethodRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfPaymentMethodRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a collection of one or more references to a  TYPE OF PAYMENT METHOD.
    """
    class Meta:
        name = "TypeOfPaymentMethodRefs_RelStructure"

    type_of_payment_method_ref: List[TypeOfPaymentMethodRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPaymentMethodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
