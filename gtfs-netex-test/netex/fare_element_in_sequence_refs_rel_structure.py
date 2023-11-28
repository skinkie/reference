from dataclasses import dataclass, field
from typing import List
from netex.access_right_in_product_ref import AccessRightInProductRef
from netex.controllable_element_in_sequence_ref import ControllableElementInSequenceRef
from netex.fare_structure_element_in_sequence_ref import FareStructureElementInSequenceRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareElementInSequenceRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a collection of one or more references to a  FARE STRUCTURE ELEMENT IN
    SEQUENCE.
    """
    class Meta:
        name = "fareElementInSequenceRefs_RelStructure"

    controllable_element_in_sequence_ref_or_fare_structure_element_in_sequence_ref_or_access_right_in_product_ref: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ControllableElementInSequenceRef",
                    "type": ControllableElementInSequenceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElementInSequenceRef",
                    "type": FareStructureElementInSequenceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessRightInProductRef",
                    "type": AccessRightInProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
