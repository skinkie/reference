from dataclasses import dataclass

from .targeted_call_structure import TargetedCallStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TargetedCall(TargetedCallStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
