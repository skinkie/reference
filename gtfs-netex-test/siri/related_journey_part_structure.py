from dataclasses import dataclass

from .journey_part_info_structure import JourneyPartInfoStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class RelatedJourneyPartStructure(JourneyPartInfoStructure):
    pass
