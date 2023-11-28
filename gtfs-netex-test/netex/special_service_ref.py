from dataclasses import dataclass
from netex.special_service_ref_structure import SpecialServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SpecialServiceRef(SpecialServiceRefStructure):
    """
    Reference to a SPECIAL SERVICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
