from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .customer_account import CustomerAccount
from .customer_account_ref import CustomerAccountRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CustomerAccountsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "customerAccounts_RelStructure"

    customer_account_ref_or_customer_account: list[Union[CustomerAccountRef, CustomerAccount]] = field(
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
