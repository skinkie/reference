from dataclasses import dataclass
from .quay_ref_structure import QuayRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class QuayRef(QuayRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
