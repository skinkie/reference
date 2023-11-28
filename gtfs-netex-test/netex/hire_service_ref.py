from dataclasses import dataclass
from netex.hire_service_ref_structure import HireServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class HireServiceRef(HireServiceRefStructure):
    """
    Identifier of an HIRE SERVICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
