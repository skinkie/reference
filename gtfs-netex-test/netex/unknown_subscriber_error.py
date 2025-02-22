from dataclasses import dataclass

from .unknown_subscriber_error_structure import UnknownSubscriberErrorStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(slots=True, kw_only=True)
class UnknownSubscriberError(UnknownSubscriberErrorStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
