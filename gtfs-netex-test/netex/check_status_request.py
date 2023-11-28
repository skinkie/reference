from dataclasses import dataclass
from netex.check_status_request_structure import CheckStatusRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class CheckStatusRequest(CheckStatusRequestStructure):
    """Request from Consumer to Producer to check whether services is working.

    Answers a CheckStatusRequest.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
