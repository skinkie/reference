from dataclasses import dataclass
from .commercial_profile_eligibility_versioned_child_structure import (
    CommercialProfileEligibilityVersionedChildStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CommercialProfileEligibility(
    CommercialProfileEligibilityVersionedChildStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
