from dataclasses import dataclass

from .service_not_available_error_structure import ServiceNotAvailableErrorStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(slots=True, kw_only=True)
class ServiceNotAvailableError(ServiceNotAvailableErrorStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
