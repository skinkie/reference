from dataclasses import dataclass

from .entity_in_version_structure import EntityInVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class EntityInVersion(EntityInVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
