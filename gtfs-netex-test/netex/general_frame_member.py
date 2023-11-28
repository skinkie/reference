from dataclasses import dataclass
from netex.general_frame_member_structure import GeneralFrameMemberStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GeneralFrameMember(GeneralFrameMemberStructure):
    """
    An association of an ENTITY in a GENERAL FRAME.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
