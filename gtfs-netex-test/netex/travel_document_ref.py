from dataclasses import dataclass
from netex.travel_document_ref_structure import TravelDocumentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TravelDocumentRef(TravelDocumentRefStructure):
    """
    Reference to a TRAVEL DOCUMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
