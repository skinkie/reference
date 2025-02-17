from dataclasses import dataclass

from .access_space_version_structure import AccessSpaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class AccessSpace(AccessSpaceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
