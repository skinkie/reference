from dataclasses import dataclass

from .travel_document_ref_structure import TravelDocumentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ServiceAccessCodeRefStructure(TravelDocumentRefStructure):
    pass
