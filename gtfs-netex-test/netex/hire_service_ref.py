from dataclasses import dataclass

from .hire_service_ref_structure import HireServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class HireServiceRef(HireServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
