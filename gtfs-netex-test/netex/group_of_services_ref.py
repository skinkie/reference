from dataclasses import dataclass

from .group_of_services_ref_structure import GroupOfServicesRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class GroupOfServicesRef(GroupOfServicesRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
