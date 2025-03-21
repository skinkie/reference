from dataclasses import dataclass

from .open_transport_mode_value_structure import OpenTransportModeValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class Submode(OpenTransportModeValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
