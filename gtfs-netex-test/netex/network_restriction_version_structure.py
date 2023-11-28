from dataclasses import dataclass, field
from netex.assignment_version_structure_1 import AssignmentVersionStructure1

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class NetworkRestrictionVersionStructure(AssignmentVersionStructure1):
    """
    Type for a NETWORK RESTRICTION.

    :ivar restricted: Whether a NETWORK RESTRICTION is allowed or
        forbidden. Default is true,, i.e.  this is a restriction..
    """
    class Meta:
        name = "NetworkRestriction_VersionStructure"

    restricted: bool = field(
        default=True,
        metadata={
            "name": "Restricted",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
