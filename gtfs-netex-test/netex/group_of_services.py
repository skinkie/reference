from dataclasses import dataclass
from .group_of_services_version_structure import (
    GroupOfServicesVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfServices(GroupOfServicesVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
