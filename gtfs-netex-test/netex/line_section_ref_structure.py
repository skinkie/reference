from dataclasses import dataclass
from .section_ref_structure import SectionRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LineSectionRefStructure(SectionRefStructure):
    value: RestrictedVar
