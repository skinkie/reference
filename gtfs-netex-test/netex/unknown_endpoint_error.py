from dataclasses import dataclass
from netex.unknown_endpoint_error_structure import UnknownEndpointErrorStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class UnknownEndpointError(UnknownEndpointErrorStructure):
    """Error: Recipient for a message to be distributed is unknown. +SIRI v2.0"""
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
