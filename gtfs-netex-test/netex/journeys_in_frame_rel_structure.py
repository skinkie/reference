from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.dated_service_journey import DatedServiceJourney
from netex.dated_vehicle_journey import DatedVehicleJourney
from netex.dead_run import DeadRun
from netex.normal_dated_vehicle_journey import NormalDatedVehicleJourney
from netex.service_journey import ServiceJourney
from netex.special_service import SpecialService
from netex.template_service_journey import TemplateServiceJourney
from netex.vehicle_journey import VehicleJourney

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneysInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of  all JOURNEYs.
    """
    class Meta:
        name = "journeysInFrame_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleJourney",
                    "type": VehicleJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DatedVehicleJourney",
                    "type": DatedVehicleJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NormalDatedVehicleJourney",
                    "type": NormalDatedVehicleJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourney",
                    "type": ServiceJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DatedServiceJourney",
                    "type": DatedServiceJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRun",
                    "type": DeadRun,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SpecialService",
                    "type": SpecialService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TemplateServiceJourney",
                    "type": TemplateServiceJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
