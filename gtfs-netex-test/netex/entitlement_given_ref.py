from dataclasses import dataclass
from netex.entitlement_given_ref_structure import EntitlementGivenRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class EntitlementGivenRef(EntitlementGivenRefStructure):
    """
    Reference to a ENTITLEMENT GIVEN PARAMETER.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
