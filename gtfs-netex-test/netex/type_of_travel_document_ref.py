from dataclasses import dataclass
from netex.type_of_travel_document_ref_structure import TypeOfTravelDocumentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfTravelDocumentRef(TypeOfTravelDocumentRefStructure):
    """
    Reference to a TYPE OF TRAVEL DOCUMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
