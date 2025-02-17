from dataclasses import dataclass

from .hire_service_version_structure import HireServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class HireService(HireServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
