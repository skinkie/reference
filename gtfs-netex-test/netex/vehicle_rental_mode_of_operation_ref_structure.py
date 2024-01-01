from dataclasses import dataclass
from .alternative_mode_of_operation_ref_structure import (
    AlternativeModeOfOperationRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleRentalModeOfOperationRefStructure(
    AlternativeModeOfOperationRefStructure
):
    value: RestrictedVar
