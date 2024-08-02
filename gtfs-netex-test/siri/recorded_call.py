from dataclasses import dataclass

from .recorded_call_structure import RecordedCallStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class RecordedCall(RecordedCallStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
