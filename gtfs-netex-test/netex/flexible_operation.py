from dataclasses import dataclass
from .flexible_mode_of_operation_value_structure import (
    FlexibleModeOfOperationValueStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleOperation(FlexibleModeOfOperationValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
