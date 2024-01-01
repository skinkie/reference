from dataclasses import dataclass
from .unknown_endpoint_error_structure import UnknownEndpointErrorStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class UnknownEndpointError(UnknownEndpointErrorStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
