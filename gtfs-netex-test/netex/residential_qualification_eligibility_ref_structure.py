from dataclasses import dataclass
from .customer_eligibility_ref_structure import CustomerEligibilityRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ResidentialQualificationEligibilityRefStructure(
    CustomerEligibilityRefStructure
):
    value: RestrictedVar
