from dataclasses import dataclass
from .single_journey_ref_structure import SingleJourneyRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SingleJourneyRef(SingleJourneyRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
