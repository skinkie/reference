from dataclasses import dataclass, field
from typing import List
from netex.frame_containment_structure import FrameContainmentStructure
from netex.service_access_code import ServiceAccessCode
from netex.service_access_code_ref import ServiceAccessCodeRef
from netex.travel_document import TravelDocument
from netex.travel_document_ref import TravelDocumentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TravelDocumentsRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of TRAVEL DOCUMENT.
    """
    class Meta:
        name = "travelDocuments_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceAccessCodeRef",
                    "type": ServiceAccessCodeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelDocumentRef",
                    "type": TravelDocumentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelDocument",
                    "type": TravelDocument,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceAccessCode",
                    "type": ServiceAccessCode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
