from dataclasses import dataclass
from .class_ref_structure import ClassRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ClassRef(ClassRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
