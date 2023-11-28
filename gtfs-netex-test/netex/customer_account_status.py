from dataclasses import dataclass, field
from netex.customer_account_status_version_structure import CustomerAccountStatusVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomerAccountStatus(CustomerAccountStatusVersionStructure):
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
