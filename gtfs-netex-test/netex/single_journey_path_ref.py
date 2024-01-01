from dataclasses import dataclass
from .single_journey_path_ref_structure import SingleJourneyPathRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SingleJourneyPathRef(SingleJourneyPathRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
