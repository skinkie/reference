from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .type_of_payment_method_ref import TypeOfPaymentMethodRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfPaymentMethodRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "TypeOfPaymentMethodRefs_RelStructure"

    type_of_payment_method_ref: list[TypeOfPaymentMethodRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPaymentMethodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
