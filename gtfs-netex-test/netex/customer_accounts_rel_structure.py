from dataclasses import dataclass, field
from typing import List, Union
from .containment_aggregation_structure import ContainmentAggregationStructure
from .customer_account import CustomerAccount
from .customer_account_ref import CustomerAccountRef


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerAccountsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "customerAccounts_RelStructure"

    customer_account_ref_or_customer_account: List[
        Union[CustomerAccountRef, CustomerAccount]
    ] = field(
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
        },
    )
