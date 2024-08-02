from dataclasses import dataclass, field
from typing import Optional

from .abstract_identified_item_structure import AbstractIdentifiedItemStructure
from .extensions_1 import Extensions1
from .monitoring_ref_structure import MonitoringRefStructure
from .targeted_vehicle_journey import TargetedVehicleJourney

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TimetabledStopVisitStructure(AbstractIdentifiedItemStructure):
    monitoring_ref: MonitoringRefStructure = field(
        metadata={
            "name": "MonitoringRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    targeted_vehicle_journey: TargetedVehicleJourney = field(
        metadata={
            "name": "TargetedVehicleJourney",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
