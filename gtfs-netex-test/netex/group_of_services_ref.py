from dataclasses import dataclass
from .group_of_services_ref_structure import GroupOfServicesRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfServicesRef(GroupOfServicesRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
