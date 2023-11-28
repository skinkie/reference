from dataclasses import dataclass, field
from typing import List
from netex.allowed_line_direction_ref import AllowedLineDirectionRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AllowedLineDirectionRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of references to an ALLOWED LINE DIRECTION.
    """
    class Meta:
        name = "allowedLineDirectionRefs_RelStructure"

    allowed_line_direction_ref: List[AllowedLineDirectionRef] = field(
        default_factory=list,
        metadata={
            "name": "AllowedLineDirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
