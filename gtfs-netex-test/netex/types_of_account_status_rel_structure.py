from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.customer_account_status import CustomerAccountStatus
from netex.customer_account_status_ref import CustomerAccountStatusRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypesOfAccountStatusRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of CUSTOMER ACCOUNT STATUSes.
    """
    class Meta:
        name = "typesOfAccountStatus_RelStructure"

    customer_account_status_ref_or_customer_account_status: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CustomerAccountStatusRef",
                    "type": CustomerAccountStatusRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerAccountStatus",
                    "type": CustomerAccountStatus,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
