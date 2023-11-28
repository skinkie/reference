from dataclasses import dataclass
from netex.companion_profile_ref_structure import CompanionProfileRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CompanionProfileRef(CompanionProfileRefStructure):
    """
    Reference to a COMPANION PROFILE usage parameter.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
