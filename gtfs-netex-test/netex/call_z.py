from dataclasses import dataclass, field
from netex.call_versioned_child_structure import CallVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CallZ(CallVersionedChildStructure):
    """A visit to a SCHEDULED STOP POINT as part of a VEHICLE JOURNEY.

    A CALL is a view of a POINT IN JOURNEY PATTERN that adds in derived
    data. No Constraints

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        name = "Call-Z"
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
