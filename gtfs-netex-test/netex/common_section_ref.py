from dataclasses import dataclass
from netex.common_section_ref_structure import CommonSectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CommonSectionRef(CommonSectionRefStructure):
    """
    Reference to a COMMON SECTION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
