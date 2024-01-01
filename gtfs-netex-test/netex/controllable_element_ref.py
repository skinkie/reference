from dataclasses import dataclass
from .controllable_element_ref_structure import ControllableElementRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ControllableElementRef(ControllableElementRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
