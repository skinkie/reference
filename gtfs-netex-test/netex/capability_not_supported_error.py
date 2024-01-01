from dataclasses import dataclass
from .capability_not_supported_error_structure import (
    CapabilityNotSupportedErrorStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class CapabilityNotSupportedError(CapabilityNotSupportedErrorStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
