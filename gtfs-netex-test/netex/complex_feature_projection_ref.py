from dataclasses import dataclass
from .complex_feature_projection_ref_structure import (
    ComplexFeatureProjectionRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ComplexFeatureProjectionRef(ComplexFeatureProjectionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
