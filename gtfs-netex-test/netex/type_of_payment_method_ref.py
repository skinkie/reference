from dataclasses import dataclass
from netex.type_of_payment_method_ref_structure import TypeOfPaymentMethodRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfPaymentMethodRef(TypeOfPaymentMethodRefStructure):
    """
    Reference to a TYPE OF PAYMENT METHOD.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
