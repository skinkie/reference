from dataclasses import dataclass

from .call_ref_structure import CallRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CallRef(CallRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
