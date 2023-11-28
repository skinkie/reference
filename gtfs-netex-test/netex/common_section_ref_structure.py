from dataclasses import dataclass
from netex.section_ref_structure import SectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CommonSectionRefStructure(SectionRefStructure):
    """
    Type for a reference to a COMMON SECTION.
    """
