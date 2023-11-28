from dataclasses import dataclass, field
from typing import Optional
from netex.error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class CapabilityNotSupportedErrorStructure(ErrorCodeStructure):
    """Type for Error: Service does not support requested capability.

    :ivar capability_ref: Id of capabiliuty that is not supported.
    """
    capability_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "CapabilityRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
