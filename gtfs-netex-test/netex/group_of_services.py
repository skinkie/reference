from dataclasses import dataclass, field
from netex.group_of_services_version_structure import GroupOfServicesVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfServices(GroupOfServicesVersionStructure):
    """
    A group of SERVICEs, often known to its users by a name or a number.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
