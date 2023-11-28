from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.stop_area_ref_structure import StopAreaRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StopAreaRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of STOP AREAs.

    :ivar stop_area_ref: Reference to the identifier of a stop area.
    """
    class Meta:
        name = "stopAreaRefs_RelStructure"

    stop_area_ref: List[StopAreaRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "StopAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
