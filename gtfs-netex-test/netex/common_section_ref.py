from dataclasses import dataclass

from .common_section_ref_structure import CommonSectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CommonSectionRef(CommonSectionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
