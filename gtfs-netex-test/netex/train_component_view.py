from dataclasses import dataclass

from .train_component_derived_view_structure import TrainComponentDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TrainComponentView(TrainComponentDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
