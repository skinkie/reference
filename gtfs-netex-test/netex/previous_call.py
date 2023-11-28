from dataclasses import dataclass, field
from netex.previous_call_versioned_child_structure import PreviousCallVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PreviousCall(PreviousCallVersionedChildStructure):
    """
    An already completed CALL of  a VEHICLE JOURNEY that occurred earlier in the
    the JOURNEY PATTERN before the current stop.

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
