from dataclasses import dataclass

from .type_of_customer_account_ref_structure import TypeOfCustomerAccountRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfCustomerAccountRef(TypeOfCustomerAccountRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
