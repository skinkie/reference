from dataclasses import dataclass
from .open_transport_mode_value_structure import (
    OpenTransportModeValueStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OpenTransportMode(OpenTransportModeValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
