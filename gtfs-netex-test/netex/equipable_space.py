from dataclasses import dataclass

from .equipable_space_version_structure import EquipableSpaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EquipableSpace(EquipableSpaceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
