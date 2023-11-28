from dataclasses import dataclass
from netex.eligibility_change_policy_ref_structure import EligibilityChangePolicyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class EligibilityChangePolicyRef(EligibilityChangePolicyRefStructure):
    """Reference to anELIGIBILITY CHANGE POLICY usage parameter.

    +v1.1
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
