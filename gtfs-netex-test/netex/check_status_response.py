from dataclasses import dataclass
from netex.check_status_response_structure import CheckStatusResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class CheckStatusResponse(CheckStatusResponseStructure):
    """Response from Producer to Consumer to inform whether services is working.

    Answers a CheckStatusRequest.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
