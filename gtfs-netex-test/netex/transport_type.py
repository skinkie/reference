from dataclasses import dataclass
from .transport_type_version_structure import TransportTypeVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TransportType(TransportTypeVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
