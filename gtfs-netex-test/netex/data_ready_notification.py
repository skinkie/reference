from dataclasses import dataclass

from .data_ready_request_structure import DataReadyRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(slots=True, kw_only=True)
class DataReadyNotification(DataReadyRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
