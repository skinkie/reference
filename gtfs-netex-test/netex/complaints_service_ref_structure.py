from dataclasses import dataclass

from .local_service_ref_structure import LocalServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ComplaintsServiceRefStructure(LocalServiceRefStructure):
    pass
