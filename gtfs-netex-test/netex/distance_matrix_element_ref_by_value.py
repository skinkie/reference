from dataclasses import dataclass
from .distance_matrix_element_ref_by_value_structure import (
    DistanceMatrixElementRefByValueStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DistanceMatrixElementRefByValue(
    DistanceMatrixElementRefByValueStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
