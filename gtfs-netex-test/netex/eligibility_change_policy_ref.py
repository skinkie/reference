from dataclasses import dataclass
from .eligibility_change_policy_ref_structure import (
    EligibilityChangePolicyRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EligibilityChangePolicyRef(EligibilityChangePolicyRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
