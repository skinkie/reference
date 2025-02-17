from dataclasses import dataclass

from .communication_service_ref_structure import CommunicationServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CommunicationServiceRef(CommunicationServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
