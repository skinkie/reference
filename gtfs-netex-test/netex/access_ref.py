from dataclasses import dataclass

from .access_ref_structure import AccessRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class AccessRef(AccessRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
