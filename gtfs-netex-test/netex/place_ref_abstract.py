from dataclasses import dataclass

from .version_of_object_ref_structure import VersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PlaceRefAbstract(VersionOfObjectRefStructure):
    class Meta:
        name = "PlaceRef_"
        namespace = "http://www.netex.org.uk/netex"
