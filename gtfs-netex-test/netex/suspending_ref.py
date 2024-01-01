from dataclasses import dataclass
from .suspending_ref_structure import SuspendingRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SuspendingRef(SuspendingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
