from dataclasses import dataclass
from netex.complaints_service_ref_structure import ComplaintsServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ComplaintsServiceRef(ComplaintsServiceRefStructure):
    """
    Identifier of an COMPLAINTS SERVICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
