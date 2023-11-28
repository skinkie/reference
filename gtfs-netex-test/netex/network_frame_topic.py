from dataclasses import dataclass
from netex.network_frame_topic_structure import NetworkFrameTopicStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class NetworkFrameTopic(NetworkFrameTopicStructure):
    """Network Object filter  Return Network Objects that match these values.

    Values are ANDed.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
