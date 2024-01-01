from dataclasses import dataclass
from .local_service_ref_structure import LocalServiceRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LocalServiceRef(LocalServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
