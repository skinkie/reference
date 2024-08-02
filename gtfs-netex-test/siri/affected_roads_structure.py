from dataclasses import dataclass, field
from typing import List, Optional

from .affected_road_structure import AffectedRoadStructure
from .group_of_locations import GroupOfLocations

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AffectedRoadsStructure:
    datex2_locations: Optional[GroupOfLocations] = field(
        default=None,
        metadata={
            "name": "Datex2Locations",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    affected_road: List[AffectedRoadStructure] = field(
        default_factory=list,
        metadata={
            "name": "AffectedRoad",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
