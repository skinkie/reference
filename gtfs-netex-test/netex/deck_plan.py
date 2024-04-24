from dataclasses import dataclass

from .deck_plan_version_structure import DeckPlanVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckPlan(DeckPlanVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
