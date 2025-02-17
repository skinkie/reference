from dataclasses import dataclass

from .travel_document_version_structure import TravelDocumentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TravelDocument(TravelDocumentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
