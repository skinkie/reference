from dataclasses import dataclass
from netex.lost_property_service_ref_structure import LostPropertyServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LostPropertyServiceRef(LostPropertyServiceRefStructure):
    """
    Identifier of an LOST PROPERTY SERVICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
