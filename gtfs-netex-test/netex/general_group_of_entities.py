from dataclasses import dataclass

from .general_group_of_entities_version_structure import GeneralGroupOfEntitiesVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class GeneralGroupOfEntities(GeneralGroupOfEntitiesVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
