from dataclasses import dataclass, field
from typing import Optional

from .payment_method_enumeration import PaymentMethodEnumeration
from .type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfPaymentMethodValueStructure(TypeOfValueVersionStructure):
    class Meta:
        name = "TypeOfPaymentMethod_ValueStructure"

    payment_method: Optional[PaymentMethodEnumeration] = field(
        default=None,
        metadata={
            "name": "PaymentMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    automated_use: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AutomatedUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
