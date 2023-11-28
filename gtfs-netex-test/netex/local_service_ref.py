from dataclasses import dataclass
from netex.local_service_ref_structure import LocalServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LocalServiceRef(LocalServiceRefStructure):
    """
    Reference to a LOCAL SERVICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
