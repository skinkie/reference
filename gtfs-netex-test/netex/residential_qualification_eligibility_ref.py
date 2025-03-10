from dataclasses import dataclass

from .residential_qualification_eligibility_ref_structure import ResidentialQualificationEligibilityRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ResidentialQualificationEligibilityRef(ResidentialQualificationEligibilityRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
