from dataclasses import dataclass
from netex.general_section_ref_structure import GeneralSectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GeneralSectionRef(GeneralSectionRefStructure):
    """
    Reference to a GENERAL SECTION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
