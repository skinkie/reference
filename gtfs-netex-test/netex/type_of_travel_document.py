from dataclasses import dataclass, field
from netex.type_of_travel_document_version_structure import TypeOfTravelDocumentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfTravelDocument(TypeOfTravelDocumentVersionStructure):
    """A classification of TRAVEL DOCUMENTs expressing their general
    functionalities and local functional characteristics specific to the operator.

    Types of TRAVEL DOCUMENTs like e.g. throw-away ticket, throw-away
    ticket unit, value card, electronic purse allowing access, public
    transport credit card etc. may be used to define these categories.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
