from dataclasses import dataclass

from .mode_of_operation_value_structure import ModeOfOperationValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class AlternativeModeOfOperationValueStructure(ModeOfOperationValueStructure):
    class Meta:
        name = "AlternativeModeOfOperation_ValueStructure"
