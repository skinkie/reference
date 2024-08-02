from dataclasses import dataclass, field
from typing import List, Optional

from .extensions_2 import Extensions2
from .installed_equipment_structure import InstalledEquipmentStructure
from .service_feature_ref_structure import ServiceFeatureRefStructure
from .validity_conditions_structure import ValidityConditionsStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass(kw_only=True)
class LocalServiceStructure(InstalledEquipmentStructure):
    validity_conditions: Optional[ValidityConditionsStructure] = field(
        default=None,
        metadata={
            "name": "ValidityConditions",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    feature_refs: Optional["LocalServiceStructure.FeatureRefs"] = field(
        default=None,
        metadata={
            "name": "FeatureRefs",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )

    @dataclass(kw_only=True)
    class FeatureRefs:
        feature_ref: List[ServiceFeatureRefStructure] = field(
            default_factory=list,
            metadata={
                "name": "FeatureRef",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/ifopt",
            },
        )
