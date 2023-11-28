from dataclasses import dataclass, field
from typing import List
from netex.destination_display_ref import DestinationDisplayRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DestinationDisplayRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of references to a DESTINATION DISPLAY.
    """
    class Meta:
        name = "destinationDisplayRefs_RelStructure"

    destination_display_ref: List[DestinationDisplayRef] = field(
        default_factory=list,
        metadata={
            "name": "DestinationDisplayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
