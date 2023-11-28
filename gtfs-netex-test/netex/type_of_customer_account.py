from dataclasses import dataclass, field
from netex.type_of_customer_account_version_structure import TypeOfCustomerAccountVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfCustomerAccount(TypeOfCustomerAccountVersionStructure):
    """
    A classification of a CUSTOMER ACCOUNT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
