from dataclasses import dataclass
from netex.error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class AllowedResourceUsageExceededErrorStructure(ErrorCodeStructure):
    """Type for error.

    AllowedResourceUsageExceeded.
    """
