from dataclasses import dataclass
from netex.type_of_entity_version_structure import TypeOfEntityVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfEntity(TypeOfEntityVersionStructure):
    """
    A Type of value used to classify an ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
