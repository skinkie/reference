from dataclasses import dataclass, field
from typing import Optional
from netex.type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfEntityVersionStructure(TypeOfValueVersionStructure):
    """Type for a TYPE OF ENTITY.

    Abstract supertype used to define open  classifications of value
    types.

    :ivar name_of_classified_entity_class: Name of Class of the ENTITY.
        Allows reflection. Fixed for each ENTITY type.
    """
    class Meta:
        name = "TypeOfEntity_VersionStructure"

    name_of_classified_entity_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameOfClassifiedEntityClass",
            "type": "Attribute",
        }
    )
