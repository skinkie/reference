from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.sales_transaction_ref import SalesTransactionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SalesTransactionRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a collection of one or more references to a SALES TRANSACTION.
    """
    class Meta:
        name = "salesTransactionRefs_RelStructure"

    sales_transaction_ref: List[SalesTransactionRef] = field(
        default_factory=list,
        metadata={
            "name": "SalesTransactionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
