from dataclasses import dataclass
from .call_versioned_child_structure import CallVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CallZ(CallVersionedChildStructure):
    class Meta:
        name = "Call-Z"
        namespace = "http://www.netex.org.uk/netex"
