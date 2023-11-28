from dataclasses import dataclass, field
from netex.type_of_payment_method_value_structure import TypeOfPaymentMethodValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfPaymentMethod(TypeOfPaymentMethodValueStructure):
    """Defines an open classification  payment methods.

    + v1.1

    :ivar id: Identifier of  TYPE OF PAYMENT METHOD.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
