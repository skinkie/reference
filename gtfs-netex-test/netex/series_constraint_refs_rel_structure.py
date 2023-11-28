from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.series_constraint_ref import SeriesConstraintRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SeriesConstraintRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a collection of one or more references to a SERIES CONSTRAINT.
    """
    class Meta:
        name = "seriesConstraintRefs_RelStructure"

    series_constraint_ref: List[SeriesConstraintRef] = field(
        default_factory=list,
        metadata={
            "name": "SeriesConstraintRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
