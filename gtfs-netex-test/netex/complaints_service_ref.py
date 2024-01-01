from dataclasses import dataclass
from .complaints_service_ref_structure import ComplaintsServiceRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ComplaintsServiceRef(ComplaintsServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
