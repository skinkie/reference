from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .dated_vehicle_journey_ref import DatedVehicleJourneyRef
from .normal_dated_vehicle_journey_ref import NormalDatedVehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ReplacedJourneysRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "replacedJourneys_RelStructure"

    dated_vehicle_journey_ref_or_normal_dated_vehicle_journey_ref: list[Union[DatedVehicleJourneyRef, NormalDatedVehicleJourneyRef]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DatedVehicleJourneyRef",
                    "type": DatedVehicleJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NormalDatedVehicleJourneyRef",
                    "type": NormalDatedVehicleJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
