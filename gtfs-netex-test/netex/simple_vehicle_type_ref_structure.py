from dataclasses import dataclass

from .transport_type_ref_structure import TransportTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SimpleVehicleTypeRefStructure(TransportTypeRefStructure):
    pass
