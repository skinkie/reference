from dataclasses import dataclass

from .estimated_call_structure import EstimatedCallStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class EstimatedCall(EstimatedCallStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
