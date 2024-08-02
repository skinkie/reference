from dataclasses import dataclass, field
from typing import List, Optional, Union

from .abstract_functional_service_request_structure import AbstractFunctionalServiceRequestStructure
from .direction_ref_structure import DirectionRefStructure
from .extensions_1 import Extensions1
from .include_translations import IncludeTranslations
from .line_ref_structure import LineRefStructure
from .vehicle_monitoring_detail_enumeration import VehicleMonitoringDetailEnumeration
from .vehicle_monitoring_ref_structure import VehicleMonitoringRefStructure
from .vehicle_ref_structure import VehicleRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class VehicleMonitoringRequestStructure(AbstractFunctionalServiceRequestStructure):
    vehicle_monitoring_ref: Optional[VehicleMonitoringRefStructure] = field(
        default=None,
        metadata={
            "name": "VehicleMonitoringRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_ref_or_line_ref: Optional[Union[VehicleRefStructure, LineRefStructure]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleRef",
                    "type": VehicleRefStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "LineRef",
                    "type": LineRefStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
    direction_ref: Optional[DirectionRefStructure] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    language: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    include_translations: Optional[IncludeTranslations] = field(
        default=None,
        metadata={
            "name": "IncludeTranslations",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    maximum_vehicles: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumVehicles",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_monitoring_detail_level: Optional[VehicleMonitoringDetailEnumeration] = field(
        default=None,
        metadata={
            "name": "VehicleMonitoringDetailLevel",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    maximum_number_of_calls: Optional["VehicleMonitoringRequestStructure.MaximumNumberOfCalls"] = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfCalls",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    include_situations: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeSituations",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    version: str = field(
        default="2.1",
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class MaximumNumberOfCalls:
        previous: Optional[int] = field(
            default=None,
            metadata={
                "name": "Previous",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        onwards: Optional[int] = field(
            default=None,
            metadata={
                "name": "Onwards",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
