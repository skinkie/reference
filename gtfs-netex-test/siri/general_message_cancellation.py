from dataclasses import dataclass

from .info_message_cancellation_structure import InfoMessageCancellationStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class GeneralMessageCancellation(InfoMessageCancellationStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
