from dataclasses import dataclass
from .group_of_entities_ref_structure_1 import GroupOfEntitiesRefStructure1


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfTimingLinksRefStructure(GroupOfEntitiesRefStructure1):
    value: RestrictedVar
