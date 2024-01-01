from dataclasses import dataclass
from .access_space_ref_structure import AccessSpaceRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessSpaceRef(AccessSpaceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
