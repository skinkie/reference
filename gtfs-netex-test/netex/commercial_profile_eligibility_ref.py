from dataclasses import dataclass
from netex.commercial_profile_eligibility_ref_structure import CommercialProfileEligibilityRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CommercialProfileEligibilityRef(CommercialProfileEligibilityRefStructure):
    """
    Reference to a COMMERCIAL PROFILE ELIGIBILITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
