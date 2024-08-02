from dataclasses import dataclass

from .info_channel_structure import InfoChannelStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class InfoChannel(InfoChannelStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
