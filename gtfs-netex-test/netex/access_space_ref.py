from dataclasses import dataclass

from .access_space_ref_structure import AccessSpaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class AccessSpaceRef(AccessSpaceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
