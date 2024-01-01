from dataclasses import dataclass
from .call_versioned_child_structure import CallVersionedChildStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Call(CallVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
