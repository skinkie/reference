from dataclasses import dataclass

from .group_of_entities_version_structure import GroupOfEntitiesVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class GroupOfEntities(GroupOfEntitiesVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
