from dataclasses import dataclass
from netex.alternative_mode_of_operation_ref_structure import AlternativeModeOfOperationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehiclePoolingModeOfOperationRefStructure(AlternativeModeOfOperationRefStructure):
    """
    Type for a reference to a VEHICLE POOLING MODE OF OPERATION.
    """
