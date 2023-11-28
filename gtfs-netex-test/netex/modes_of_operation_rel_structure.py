from dataclasses import dataclass, field
from typing import List
from netex.alternative_mode_of_operation import AlternativeModeOfOperation
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.flexible_operation import FlexibleOperation
from netex.personal_mode_of_operation import PersonalModeOfOperation
from netex.scheduled_operation import ScheduledOperation
from netex.vehicle_pooling import VehiclePooling
from netex.vehicle_rental import VehicleRental
from netex.vehicle_sharing import VehicleSharing

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ModesOfOperationRelStructure(ContainmentAggregationStructure):
    """
    SUBMODEs  associated with entity.
    """
    class Meta:
        name = "modesOfOperationRelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PersonalModeOfOperation",
                    "type": PersonalModeOfOperation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AlternativeModeOfOperation",
                    "type": AlternativeModeOfOperation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePooling",
                    "type": VehiclePooling,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharing",
                    "type": VehicleSharing,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleRental",
                    "type": VehicleRental,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleOperation",
                    "type": FlexibleOperation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledOperation",
                    "type": ScheduledOperation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
