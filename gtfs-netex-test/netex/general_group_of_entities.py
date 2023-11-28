from dataclasses import dataclass, field
from netex.general_group_of_entities_version_structure import GeneralGroupOfEntitiesVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GeneralGroupOfEntities(GeneralGroupOfEntitiesVersionStructure):
    """
    A grouping of ENTITies which will be commonly referenced for a specific
    purpose.

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
