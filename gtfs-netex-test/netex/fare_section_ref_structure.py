from dataclasses import dataclass
from .general_section_ref_structure import GeneralSectionRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareSectionRefStructure(GeneralSectionRefStructure):
    value: RestrictedVar
