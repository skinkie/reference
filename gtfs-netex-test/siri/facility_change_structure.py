from dataclasses import dataclass, field
from typing import Optional

from .equipment_availability_structure import EquipmentAvailabilityStructure
from .mobility_disruption_structure import MobilityDisruptionStructure
from .situation_ref import SituationRef

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class FacilityChangeStructure:
    equipment_availability: Optional[EquipmentAvailabilityStructure] = field(
        default=None,
        metadata={
            "name": "EquipmentAvailability",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_ref: Optional[SituationRef] = field(
        default=None,
        metadata={
            "name": "SituationRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    mobility_disruption: Optional[MobilityDisruptionStructure] = field(
        default=None,
        metadata={
            "name": "MobilityDisruption",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
