from dataclasses import dataclass, field
from typing import Optional
from netex.on_becoming_enumeration import OnBecomingEnumeration
from netex.on_ceasing_enumeration import OnCeasingEnumeration
from netex.usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class EligibilityChangePolicyVersionStructure(UsageParameterVersionStructure):
    """
    Type for ELIGIBILITY CHANGE POLICY.

    :ivar on_becoming_eligible_policy: Policy to apply onproduct holder
        becoming eligible.
    :ivar on_ceasing_to_be_eligible_policy: Policy to apply on product
        holder  ceasing to be eligible.
    """
    class Meta:
        name = "EligibilityChangePolicy_VersionStructure"

    on_becoming_eligible_policy: Optional[OnBecomingEnumeration] = field(
        default=None,
        metadata={
            "name": "OnBecomingEligiblePolicy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    on_ceasing_to_be_eligible_policy: Optional[OnCeasingEnumeration] = field(
        default=None,
        metadata={
            "name": "OnCeasingToBeEligiblePolicy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
