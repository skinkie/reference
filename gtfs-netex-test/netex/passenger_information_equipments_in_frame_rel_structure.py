from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .passenger_information_equipment import PassengerInformationEquipment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PassengerInformationEquipmentsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "passengerInformationEquipmentsInFrame_RelStructure"

    passenger_information_equipment: list[PassengerInformationEquipment] = field(
        default_factory=list,
        metadata={
            "name": "PassengerInformationEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
