from dataclasses import dataclass, field
from typing import List
from netex.destination_display_variant_ref import DestinationDisplayVariantRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DestinationDisplayVariantRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of references to a DESTINATION DISPLAY VARIANT.
    """
    class Meta:
        name = "destinationDisplayVariantRefs_RelStructure"

    destination_display_variant_ref: List[DestinationDisplayVariantRef] = field(
        default_factory=list,
        metadata={
            "name": "DestinationDisplayVariantRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
