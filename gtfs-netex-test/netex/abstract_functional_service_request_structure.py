from dataclasses import dataclass
from .abstract_service_request_structure import AbstractServiceRequestStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractFunctionalServiceRequestStructure(
    AbstractServiceRequestStructure
):
    pass
