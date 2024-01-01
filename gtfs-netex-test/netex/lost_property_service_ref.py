from dataclasses import dataclass
from .lost_property_service_ref_structure import (
    LostPropertyServiceRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LostPropertyServiceRef(LostPropertyServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
