from dataclasses import dataclass
from .lost_property_service_version_structure import (
    LostPropertyServiceVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LostPropertyService(LostPropertyServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
