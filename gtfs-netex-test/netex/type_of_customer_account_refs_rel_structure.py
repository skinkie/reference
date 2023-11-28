from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.type_of_customer_account_ref import TypeOfCustomerAccountRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfCustomerAccountRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of TYPEs OF CUSTOMER ACCOUNT .
    """
    class Meta:
        name = "typeOfCustomerAccountRefs_RelStructure"

    type_of_customer_account_ref: List[TypeOfCustomerAccountRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfCustomerAccountRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
