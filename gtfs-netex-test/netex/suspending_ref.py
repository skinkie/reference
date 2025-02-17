from dataclasses import dataclass

from .suspending_ref_structure import SuspendingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SuspendingRef(SuspendingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
