from dataclasses import dataclass
from .capabilities_response_structure import CapabilitiesResponseStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class CapabilitiesResponse(CapabilitiesResponseStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
