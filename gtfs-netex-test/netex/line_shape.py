from dataclasses import dataclass
from .line_shape_structure_2 import LineShapeStructure2


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LineShape(LineShapeStructure2):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
