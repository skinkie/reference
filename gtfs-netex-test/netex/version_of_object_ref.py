from dataclasses import dataclass

from .version_of_object_ref_structure import VersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VersionOfObjectRef(VersionOfObjectRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
