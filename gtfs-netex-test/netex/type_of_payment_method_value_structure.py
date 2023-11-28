from dataclasses import dataclass, field
from typing import Optional
from netex.payment_method_enumeration import PaymentMethodEnumeration
from netex.type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfPaymentMethodValueStructure(TypeOfValueVersionStructure):
    """
    Type for a TYPE OF TYPE OF PAYMENT METHOD.

    :ivar payment_method: Payment method value.
    :ivar automated_use: Whether PAYMENT METHOD can be used for
        automated payments.
    """
    class Meta:
        name = "TypeOfPaymentMethod_ValueStructure"

    payment_method: Optional[PaymentMethodEnumeration] = field(
        default=None,
        metadata={
            "name": "PaymentMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    automated_use: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AutomatedUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
