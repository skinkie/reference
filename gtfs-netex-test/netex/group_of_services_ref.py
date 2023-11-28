from dataclasses import dataclass
from netex.group_of_services_ref_structure import GroupOfServicesRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfServicesRef(GroupOfServicesRefStructure):
    """
    Reference to a GROUP OF SERVICEs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
