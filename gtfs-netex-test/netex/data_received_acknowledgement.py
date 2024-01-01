from dataclasses import dataclass
from .data_received_response_structure import DataReceivedResponseStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class DataReceivedAcknowledgement(DataReceivedResponseStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
