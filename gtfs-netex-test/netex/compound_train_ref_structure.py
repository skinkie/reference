from dataclasses import dataclass
from netex.vehicle_type_ref_structure import VehicleTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CompoundTrainRefStructure(VehicleTypeRefStructure):
    """
    Type for a reference to a COMPOUND TRAIN.
    """
