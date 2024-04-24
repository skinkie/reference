from dataclasses import dataclass

from .deck_plan_ref_structure import DeckPlanRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckPlanRef(DeckPlanRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
