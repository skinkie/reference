from dataclasses import dataclass
from .mode_of_operation_ref_structure import ModeOfOperationRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ConventionalModeOfOperationRefStructure(ModeOfOperationRefStructure):
    value: RestrictedVar
