from dataclasses import dataclass

from .data_received_response_structure import DataReceivedResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(slots=True, kw_only=True)
class DataReceivedAcknowledgement(DataReceivedResponseStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
