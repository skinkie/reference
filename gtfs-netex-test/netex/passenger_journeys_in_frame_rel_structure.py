from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .dated_service_journey import DatedServiceJourney
from .service_journey import ServiceJourney
from .special_service import SpecialService
from .template_service_journey import TemplateServiceJourney

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerJourneysInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "passengerJourneysInFrame_RelStructure"

    dated_service_journey_or_service_journey_or_special_service_or_template_service_journey: list[Union[DatedServiceJourney, ServiceJourney, SpecialService, TemplateServiceJourney]] = field(
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
        },
    )
