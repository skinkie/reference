from dataclasses import dataclass
from netex.publication_request_structure import PublicationRequestStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PublicationRequest(PublicationRequestStructure):
    """A bulk publication request for NeTEx objects specifying which elements
    should be returned.

    Can be echoed back in a publication response.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
