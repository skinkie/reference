from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional, Union

from .availability_condition_ref import AvailabilityConditionRef
from .call_ref_structure import CallRefStructure
from .restricted_service_facility_set_ref import RestrictedServiceFacilitySetRef
from .service_facility_set_ref import ServiceFacilitySetRef
from .service_facility_set_version_structure import ServiceFacilitySetVersionStructure
from .stop_point_in_journey_pattern_ref_structure import StopPointInJourneyPatternRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RestrictedServiceFacilitySetVersionStructure(ServiceFacilitySetVersionStructure):
    class Meta:
        name = "RestrictedServiceFacilitySet_VersionStructure"

    service_facility_set_ref: Optional[Union[RestrictedServiceFacilitySetRef, ServiceFacilitySetRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RestrictedServiceFacilitySetRef",
                    "type": RestrictedServiceFacilitySetRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceFacilitySetRef",
                    "type": ServiceFacilitySetRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    from_call_or_to_call_or_from_stop_point_in_journey_pattern_or_to_stop_point_in_journey_pattern: List[
        Union["RestrictedServiceFacilitySetVersionStructure.FromCall", "RestrictedServiceFacilitySetVersionStructure.ToCall", "RestrictedServiceFacilitySetVersionStructure.FromStopPointInJourneyPattern", "RestrictedServiceFacilitySetVersionStructure.ToStopPointInJourneyPattern"]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FromCall",
                    "type": ForwardRef("RestrictedServiceFacilitySetVersionStructure.FromCall"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ToCall",
                    "type": ForwardRef("RestrictedServiceFacilitySetVersionStructure.ToCall"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FromStopPointInJourneyPattern",
                    "type": ForwardRef("RestrictedServiceFacilitySetVersionStructure.FromStopPointInJourneyPattern"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ToStopPointInJourneyPattern",
                    "type": ForwardRef("RestrictedServiceFacilitySetVersionStructure.ToStopPointInJourneyPattern"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 2,
        },
    )
    availability_condition_ref: Optional[AvailabilityConditionRef] = field(
        default=None,
        metadata={
            "name": "AvailabilityConditionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )

    @dataclass(kw_only=True)
    class FromCall(CallRefStructure):
        pass

    @dataclass(kw_only=True)
    class ToCall(CallRefStructure):
        pass

    @dataclass(kw_only=True)
    class FromStopPointInJourneyPattern(StopPointInJourneyPatternRefStructure):
        pass

    @dataclass(kw_only=True)
    class ToStopPointInJourneyPattern(StopPointInJourneyPatternRefStructure):
        pass
