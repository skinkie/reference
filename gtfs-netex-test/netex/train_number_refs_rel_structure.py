from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.train_number_ref import TrainNumberRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TrainNumberRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of TRAIN NUMBERs.
    """
    class Meta:
        name = "trainNumberRefs_RelStructure"

    train_number_ref: List[TrainNumberRef] = field(
        default_factory=list,
        metadata={
            "name": "TrainNumberRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
