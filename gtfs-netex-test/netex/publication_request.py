from dataclasses import dataclass
from .publication_request_structure import PublicationRequestStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PublicationRequest(PublicationRequestStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
