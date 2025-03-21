from dataclasses import dataclass

from .section_ref_structure import SectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ParentSectionRef(SectionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
