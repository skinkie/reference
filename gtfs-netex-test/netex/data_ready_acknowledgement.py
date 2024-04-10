from dataclasses import dataclass

from .data_ready_response_structure import DataReadyResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class DataReadyAcknowledgement(DataReadyResponseStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
