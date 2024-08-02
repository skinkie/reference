from dataclasses import dataclass

from .info_message_structure import InfoMessageStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class GeneralMessage(InfoMessageStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
