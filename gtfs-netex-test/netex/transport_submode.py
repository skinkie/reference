from dataclasses import dataclass
from netex.transport_submode_structure import TransportSubmodeStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TransportSubmode(TransportSubmodeStructure):
    """
    A submode of a Public Transport MODE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
