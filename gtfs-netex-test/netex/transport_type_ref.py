from dataclasses import dataclass
from .transport_type_ref_structure import TransportTypeRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TransportTypeRef(TransportTypeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
