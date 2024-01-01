from dataclasses import dataclass
from .check_status_request_structure import CheckStatusRequestStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class CheckStatusRequest(CheckStatusRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
