from dataclasses import dataclass
from .type_of_service_feature_ref_structure import (
    TypeOfServiceFeatureRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfServiceFeatureRef(TypeOfServiceFeatureRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
