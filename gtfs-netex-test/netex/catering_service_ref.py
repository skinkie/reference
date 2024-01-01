from dataclasses import dataclass
from .catering_service_ref_structure import CateringServiceRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CateringServiceRef(CateringServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
