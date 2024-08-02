from dataclasses import dataclass, field
from typing import List, Optional

from .abstract_item_structure import AbstractItemStructure
from .estimated_service_journey_interchange import EstimatedServiceJourneyInterchange
from .estimated_vehicle_journey import EstimatedVehicleJourney
from .version_ref import VersionRef

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class EstimatedVersionFrameStructure(AbstractItemStructure):
    version_ref: Optional[VersionRef] = field(
        default=None,
        metadata={
            "name": "VersionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    estimated_vehicle_journey: List[EstimatedVehicleJourney] = field(
        default_factory=list,
        metadata={
            "name": "EstimatedVehicleJourney",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
    estimated_service_journey_interchange: List[EstimatedServiceJourneyInterchange] = field(
        default_factory=list,
        metadata={
            "name": "EstimatedServiceJourneyInterchange",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
