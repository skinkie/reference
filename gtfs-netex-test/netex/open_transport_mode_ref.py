from dataclasses import dataclass
from .open_transport_mode_ref_structure import OpenTransportModeRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OpenTransportModeRef(OpenTransportModeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
