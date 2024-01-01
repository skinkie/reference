from dataclasses import dataclass
from .previous_call_versioned_child_structure import (
    PreviousCallVersionedChildStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PreviousCall(PreviousCallVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
