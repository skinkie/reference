from dataclasses import dataclass

from .stop_notice_cancellation_structure import StopNoticeCancellationStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopNoticeCancellation(StopNoticeCancellationStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
