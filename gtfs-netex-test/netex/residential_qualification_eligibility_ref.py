from dataclasses import dataclass
from netex.residential_qualification_eligibility_ref_structure import ResidentialQualificationEligibilityRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ResidentialQualificationEligibilityRef(ResidentialQualificationEligibilityRefStructure):
    """
    Reference to a RESIDENTIAL QUALIFICATION ELIGIBILIT..
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
