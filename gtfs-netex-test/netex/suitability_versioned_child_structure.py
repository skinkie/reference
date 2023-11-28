from dataclasses import dataclass, field
from netex.suitable_enumeration import SuitableEnumeration
from netex.user_need_versioned_child_structure import UserNeedVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SuitabilityVersionedChildStructure(UserNeedVersionedChildStructure):
    """
    Type for SUITABILITY.

    :ivar suitable: Whether the facility is suitable.
    """
    class Meta:
        name = "Suitability_VersionedChildStructure"

    suitable: SuitableEnumeration = field(
        metadata={
            "name": "Suitable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
