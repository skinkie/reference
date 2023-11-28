from dataclasses import dataclass, field
from typing import List
from netex.customer_account_status_ref import CustomerAccountStatusRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomerAccountStatusRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of CUSTOMER ACCOUNT STATUSES.
    """
    class Meta:
        name = "customerAccountStatusRefs_RelStructure"

    customer_account_status_ref: List[CustomerAccountStatusRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerAccountStatusRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
