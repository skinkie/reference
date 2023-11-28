from dataclasses import dataclass
from netex.unapproved_key_access_structure import UnapprovedKeyAccessStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class UnapprovedKeyAccessError(UnapprovedKeyAccessStructure):
    """Error: Recipient of a message to be distributed is not available. +SIRI v2.0"""
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
