from dataclasses import dataclass

from .catering_service_ref_structure import CateringServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CateringServiceRef(CateringServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
