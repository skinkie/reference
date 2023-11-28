from dataclasses import dataclass
from netex.commercial_profile_ref_structure import CommercialProfileRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CommercialProfileRef(CommercialProfileRefStructure):
    """
    Reference to a COMMERCIAL PROFILE usage parameter.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
