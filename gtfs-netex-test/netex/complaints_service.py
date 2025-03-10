from dataclasses import dataclass

from .complaints_service_version_structure import ComplaintsServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ComplaintsService(ComplaintsServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
