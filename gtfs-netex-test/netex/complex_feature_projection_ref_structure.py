from dataclasses import dataclass
from .projection_ref_structure import ProjectionRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ComplexFeatureProjectionRefStructure(ProjectionRefStructure):
    value: RestrictedVar
