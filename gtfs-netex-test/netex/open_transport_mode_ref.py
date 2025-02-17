from dataclasses import dataclass

from .open_transport_mode_ref_structure import OpenTransportModeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class OpenTransportModeRef(OpenTransportModeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
