from dataclasses import dataclass
from .access_space_version_structure import AccessSpaceVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessSpace(AccessSpaceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
