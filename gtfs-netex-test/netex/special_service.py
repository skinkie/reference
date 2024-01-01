from dataclasses import dataclass
from .special_service_version_structure import SpecialServiceVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SpecialService(SpecialServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
