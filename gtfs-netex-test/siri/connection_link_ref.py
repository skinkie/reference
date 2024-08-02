from dataclasses import dataclass

from .connection_link_ref_structure import ConnectionLinkRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ConnectionLinkRef(ConnectionLinkRefStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
