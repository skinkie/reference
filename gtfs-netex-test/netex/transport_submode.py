from dataclasses import dataclass

from .transport_submode_structure import TransportSubmodeStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TransportSubmode(TransportSubmodeStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
