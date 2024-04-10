from dataclasses import dataclass

from .abstract_service_request_structure import AbstractServiceRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractFunctionalServiceRequestStructure(AbstractServiceRequestStructure):
    pass
