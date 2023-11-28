from dataclasses import dataclass
from netex.customer_eligibility_ref_structure import CustomerEligibilityRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CommercialProfileEligibilityRefStructure(CustomerEligibilityRefStructure):
    """
    Type for Reference to a COMMERCIAL PROFILE ELIGIBILITY.
    """
