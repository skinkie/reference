from dataclasses import dataclass
from netex.transport_type_ref_structure import TransportTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleTypeRefStructure(TransportTypeRefStructure):
    """
    Type for a reference to a VEHICLE TYPE.
    """
