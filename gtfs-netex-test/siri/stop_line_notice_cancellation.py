from dataclasses import dataclass

from .stop_line_notice_cancellation_structure import StopLineNoticeCancellationStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopLineNoticeCancellation(StopLineNoticeCancellationStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
