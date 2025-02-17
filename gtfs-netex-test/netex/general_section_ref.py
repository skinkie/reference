from dataclasses import dataclass

from .general_section_ref_structure import GeneralSectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class GeneralSectionRef(GeneralSectionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
