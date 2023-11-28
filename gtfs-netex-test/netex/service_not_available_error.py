from dataclasses import dataclass
from netex.service_not_available_error_structure import ServiceNotAvailableErrorStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceNotAvailableError(ServiceNotAvailableErrorStructure):
    """Error: Functional service is not available to use (but it is still capable of giving this response)."""
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
