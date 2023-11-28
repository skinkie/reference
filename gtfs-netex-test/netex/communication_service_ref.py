from dataclasses import dataclass
from netex.communication_service_ref_structure import CommunicationServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CommunicationServiceRef(CommunicationServiceRefStructure):
    """
    Identifier of an COMMUNICATION SERVICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
