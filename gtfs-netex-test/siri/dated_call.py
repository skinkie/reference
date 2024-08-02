from dataclasses import dataclass

from .dated_call_structure import DatedCallStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class DatedCall(DatedCallStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
