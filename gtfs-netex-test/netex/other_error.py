from dataclasses import dataclass
from netex.other_error_structure import OtherErrorStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class OtherError(OtherErrorStructure):
    """Error: Error type other than the well defined codes."""
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
