from dataclasses import dataclass, field
from typing import List, Optional

from .compliance_option_enum import ComplianceOptionEnum
from .direction_enum import DirectionEnum
from .extension_type import ExtensionType
from .operator_action import OperatorAction
from .places_enum import PlacesEnum
from .traffic_type_enum import TrafficTypeEnum
from .vehicle_characteristics import VehicleCharacteristics

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class NetworkManagement(OperatorAction):
    compliance_option: ComplianceOptionEnum = field(
        metadata={
            "name": "complianceOption",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    applicable_for_traffic_direction: List[DirectionEnum] = field(
        default_factory=list,
        metadata={
            "name": "applicableForTrafficDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    applicable_for_traffic_type: List[TrafficTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "applicableForTrafficType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    places_at_which_applicable: List[PlacesEnum] = field(
        default_factory=list,
        metadata={
            "name": "placesAtWhichApplicable",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    automatically_initiated: Optional[bool] = field(
        default=None,
        metadata={
            "name": "automaticallyInitiated",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    for_vehicles_with_characteristics_of: List[VehicleCharacteristics] = field(
        default_factory=list,
        metadata={
            "name": "forVehiclesWithCharacteristicsOf",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    network_management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "networkManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
