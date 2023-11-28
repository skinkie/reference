from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.customer_account import CustomerAccount
from netex.customer_account_ref import CustomerAccountRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomerAccountsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of CUSTOMER ACCOUNTs.
    """
    class Meta:
        name = "customerAccounts_RelStructure"

    customer_account_ref_or_customer_account: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CustomerAccountRef",
                    "type": CustomerAccountRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerAccount",
                    "type": CustomerAccount,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
