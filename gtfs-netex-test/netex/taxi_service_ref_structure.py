from dataclasses import dataclass
from netex.vehicle_pooling_service_ref_structure import VehiclePoolingServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TaxiServiceRefStructure(VehiclePoolingServiceRefStructure):
    """
    Type for a reference to an TAXI SERVICE.
    """
