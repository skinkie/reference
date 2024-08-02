from dataclasses import dataclass

from .service_exception_structure import ServiceExceptionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ServiceException(ServiceExceptionStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
