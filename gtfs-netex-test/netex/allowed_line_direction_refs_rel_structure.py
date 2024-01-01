from dataclasses import dataclass, field
from typing import List
from .allowed_line_direction_ref import AllowedLineDirectionRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AllowedLineDirectionRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "allowedLineDirectionRefs_RelStructure"

    allowed_line_direction_ref: List[AllowedLineDirectionRef] = field(
        default_factory=list,
        metadata={
            "name": "AllowedLineDirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
