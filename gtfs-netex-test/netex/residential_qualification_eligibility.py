from dataclasses import dataclass
from .residential_qualification_eligibility_versioned_child_structure import (
    ResidentialQualificationEligibilityVersionedChildStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ResidentialQualificationEligibility(
    ResidentialQualificationEligibilityVersionedChildStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
