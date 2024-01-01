from dataclasses import dataclass
from .access_ref_structure import AccessRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessRef(AccessRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
