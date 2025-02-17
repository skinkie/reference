from dataclasses import dataclass

from .customer_eligibility_versioned_child_structure import CustomerEligibilityVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CustomerEligibility1(CustomerEligibilityVersionedChildStructure):
    class Meta:
        name = "CustomerEligibility"
        namespace = "http://www.netex.org.uk/netex"
