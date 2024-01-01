from dataclasses import dataclass
from .train_component_derived_view_structure import (
    TrainComponentDerivedViewStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainComponentView(TrainComponentDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
