from dataclasses import dataclass
from netex.type_of_customer_account_ref_structure import TypeOfCustomerAccountRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfCustomerAccountRef(TypeOfCustomerAccountRefStructure):
    """
    Reference to a TYPE OF CUSTOMER ACCOUNT .
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
