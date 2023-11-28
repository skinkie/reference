from dataclasses import dataclass
from netex.capability_not_supported_error_structure import CapabilityNotSupportedErrorStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class CapabilityNotSupportedError(CapabilityNotSupportedErrorStructure):
    """Error: Service does not support the requested capability."""
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
