from dataclasses import dataclass, field
from netex.user_need_versioned_child_structure import UserNeedVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class UserNeed(UserNeedVersionedChildStructure):
    """
    A user's need for a particular SUITABILITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
