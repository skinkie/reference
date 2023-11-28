from dataclasses import dataclass, field
from netex.customer_account_version_structure import CustomerAccountVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomerAccount(CustomerAccountVersionStructure):
    """A contract with a particular (but possibly anonymous) customer, ruling the
    consumption of transport services (and joint services).

    A CUSTOMER ACCOUNT may be designed for a fixed SALES OFFER PACKAGE
    (e.g. ticket) or to allow successive purchases of SALES OFFER
    PACKAGEs.

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
