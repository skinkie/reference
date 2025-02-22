from dataclasses import dataclass, field

from .destination_display_variant_ref import DestinationDisplayVariantRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DestinationDisplayVariantRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "destinationDisplayVariantRefs_RelStructure"

    destination_display_variant_ref: list[DestinationDisplayVariantRef] = field(
        default_factory=list,
        metadata={
            "name": "DestinationDisplayVariantRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
