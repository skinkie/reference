from dataclasses import dataclass

from .lost_property_service_version_structure import LostPropertyServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class LostPropertyService(LostPropertyServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
