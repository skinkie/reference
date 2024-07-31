from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .fare_contract_entries_rel_structure import SalesTransaction
from .sales_transaction_ref import SalesTransactionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SalesTransactionsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "salesTransactions_RelStructure"

    sales_transaction_ref_or_sales_transaction: List[Union[SalesTransactionRef, SalesTransaction]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SalesTransactionRef",
                    "type": SalesTransactionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesTransaction",
                    "type": SalesTransaction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
