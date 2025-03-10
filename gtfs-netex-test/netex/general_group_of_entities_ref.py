from dataclasses import dataclass

from .general_group_of_entities_ref_structure import GeneralGroupOfEntitiesRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class GeneralGroupOfEntitiesRef(GeneralGroupOfEntitiesRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
