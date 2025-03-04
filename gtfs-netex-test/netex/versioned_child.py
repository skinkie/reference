from dataclasses import dataclass

from .entity_in_version_structure import VersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VersionedChild(VersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
