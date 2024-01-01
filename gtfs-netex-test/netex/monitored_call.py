from dataclasses import dataclass
from .monitored_call_versioned_child_structure import (
    MonitoredCallVersionedChildStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MonitoredCall(MonitoredCallVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
