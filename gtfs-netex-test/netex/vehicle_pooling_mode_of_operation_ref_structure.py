from dataclasses import dataclass

from .alternative_mode_of_operation_ref_structure import (
    AlternativeModeOfOperationRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehiclePoolingModeOfOperationRefStructure(
    AlternativeModeOfOperationRefStructure
):
    pass
