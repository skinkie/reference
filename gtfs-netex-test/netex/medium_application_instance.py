from dataclasses import dataclass, field
from netex.medium_application_instance_versioned_child_structure import MediumApplicationInstanceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MediumApplicationInstance(MediumApplicationInstanceVersionedChildStructure):
    """Initialized instance of a software  application that runs on a MEDIUM ACCESS
    DEVICE.

    +v1.2.2

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
