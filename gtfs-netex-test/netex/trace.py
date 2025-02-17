from dataclasses import dataclass

from .trace_structure import TraceStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class Trace(TraceStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
