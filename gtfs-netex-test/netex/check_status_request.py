from dataclasses import dataclass

from .check_status_request_structure import CheckStatusRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(slots=True, kw_only=True)
class CheckStatusRequest(CheckStatusRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
