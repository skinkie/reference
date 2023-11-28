from dataclasses import dataclass
from netex.entitlement_required_ref_structure import EntitlementRequiredRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class EntitlementRequiredRef(EntitlementRequiredRefStructure):
    """
    Reference to a ENTITLEMENT REQUIRED PARAMETER.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
