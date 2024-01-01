from dataclasses import dataclass
from .penalty_policy_ref_structure import PenaltyPolicyRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PenaltyPolicyRef(PenaltyPolicyRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
