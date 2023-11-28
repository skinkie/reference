from dataclasses import dataclass
from netex.transport_type_ref_structure import TransportTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TransportTypeRef(TransportTypeRefStructure):
    """Reference to a TRANSPORT TYPE.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
