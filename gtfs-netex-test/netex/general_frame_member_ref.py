from dataclasses import dataclass
from netex.general_frame_member_ref_structure import GeneralFrameMemberRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GeneralFrameMemberRef(GeneralFrameMemberRefStructure):
    """
    Reference to a GENERAL FRAME MEMBER.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
