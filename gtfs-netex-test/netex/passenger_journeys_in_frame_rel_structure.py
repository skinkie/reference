from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.dated_service_journey import DatedServiceJourney
from netex.service_journey import ServiceJourney
from netex.special_service import SpecialService
from netex.template_service_journey import TemplateServiceJourney

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PassengerJourneysInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of  passenger  JOURNEYs.
    """
    class Meta:
        name = "passengerJourneysInFrame_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DatedServiceJourney",
                    "type": DatedServiceJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourney",
                    "type": ServiceJourney,
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
