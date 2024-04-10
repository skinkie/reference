from dataclasses import dataclass

from .customer_eligibility_ref_structure import CustomerEligibilityRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ResidentialQualificationEligibilityRefStructure(CustomerEligibilityRefStructure):
    pass
