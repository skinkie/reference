from dataclasses import dataclass, field
from netex.eligibility_change_policy_version_structure import EligibilityChangePolicyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class EligibilityChangePolicy(EligibilityChangePolicyVersionStructure):
    """
    The policy to apply  if ta user's eligibility as a USER PROFILE changes.

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
