from dataclasses import dataclass
from .line_section_ref_structure import LineSectionRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LineSectionRef(LineSectionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
