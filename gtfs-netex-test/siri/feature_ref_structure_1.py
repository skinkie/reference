from dataclasses import dataclass, field
from typing import Optional

from .feature_id_ref_structure import FeatureIdRefStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass(kw_only=True)
class FeatureRefStructure1:
    class Meta:
        name = "FeatureRefStructure"

    feature_id_ref: FeatureIdRefStructure = field(
        metadata={
            "name": "FeatureIdRef",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "required": True,
        }
    )
    feature_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "FeatureType",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
