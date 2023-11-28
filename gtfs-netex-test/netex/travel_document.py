from dataclasses import dataclass, field
from netex.travel_document_version_structure import TravelDocumentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TravelDocument(TravelDocumentVersionStructure):
    """
    A particular physical support (ticket, card...) to be held by a customer,
    allowing the right to travel or to consume joint-services, to proof a payment
    (including possible discount rights), to store a subset of the FARE CONTRACT
    liabilities or a combination of those.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
