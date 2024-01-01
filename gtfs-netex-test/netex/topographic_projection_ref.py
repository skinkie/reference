from dataclasses import dataclass
from .topographic_projection_ref_structure import (
    TopographicProjectionRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TopographicProjectionRef(TopographicProjectionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
