from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.validity_trigger_ref import ValidityTriggerRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ValidityTriggerRefsRelStructure(OneToManyRelationshipStructure):
    """
    A collection of one or more VALIDITY TRIGGERs.
    """
    class Meta:
        name = "validityTriggerRefs_RelStructure"

    validity_trigger_ref: List[ValidityTriggerRef] = field(
        default_factory=list,
        metadata={
            "name": "ValidityTriggerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
