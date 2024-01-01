from dataclasses import dataclass
from .capabilities_request_structure import CapabilitiesRequestStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class CapabilitiesRequest(CapabilitiesRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
