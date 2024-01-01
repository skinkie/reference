from dataclasses import dataclass
from .class_of_use_ref_structure import ClassOfUseRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ClassOfUseRef(ClassOfUseRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
