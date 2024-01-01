from dataclasses import dataclass
from .hire_service_version_structure import HireServiceVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class HireService(HireServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
