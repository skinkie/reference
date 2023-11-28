from dataclasses import dataclass, field
from typing import List
from netex.flexible_line_ref import FlexibleLineRef
from netex.line_ref import LineRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LineRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of references to a LINE.
    """
    class Meta:
        name = "lineRefs_RelStructure"

    flexible_line_ref_or_line_ref: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleLineRef",
                    "type": FlexibleLineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineRef",
                    "type": LineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
