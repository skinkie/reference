from dataclasses import dataclass

from .priceable_object_version_structure import TimeStructureFactorVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TimeStructureFactor(TimeStructureFactorVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
