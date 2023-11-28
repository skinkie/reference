from dataclasses import dataclass
from netex.unknown_subscriber_error_structure import UnknownSubscriberErrorStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class UnknownSubscriberError(UnknownSubscriberErrorStructure):
    """Error: Subscriber not found."""
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
