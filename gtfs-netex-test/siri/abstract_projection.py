from dataclasses import dataclass, field
from typing import List, Optional

from .feature_ref_structure_1 import FeatureRefStructure1

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass(kw_only=True)
class AbstractProjection:
    features: Optional["AbstractProjection.Features"] = field(
        default=None,
        metadata={
            "name": "Features",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )

    @dataclass(kw_only=True)
    class Features:
        gis_feature_ref: List[FeatureRefStructure1] = field(
            default_factory=list,
            metadata={
                "name": "GisFeatureRef",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/ifopt",
                "min_occurs": 1,
            },
        )
