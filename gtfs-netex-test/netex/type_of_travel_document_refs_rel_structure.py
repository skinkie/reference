from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.type_of_travel_document_ref import TypeOfTravelDocumentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfTravelDocumentRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of TYPEs OF TRAVEL DOCUMENT.
    """
    class Meta:
        name = "TypeOfTravelDocumentRefs_RelStructure"

    type_of_travel_document_ref: List[TypeOfTravelDocumentRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfTravelDocumentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
