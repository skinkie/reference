from dataclasses import dataclass
from .general_group_of_entities_ref_structure import (
    GeneralGroupOfEntitiesRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeneralGroupOfEntitiesRef(GeneralGroupOfEntitiesRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
