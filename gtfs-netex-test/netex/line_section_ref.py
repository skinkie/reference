from dataclasses import dataclass
from netex.line_section_ref_structure import LineSectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LineSectionRef(LineSectionRefStructure):
    """
    Reference to a LINE SECTION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
