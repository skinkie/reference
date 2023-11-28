from dataclasses import dataclass, field
from typing import List
from netex.availability_condition_ref import AvailabilityConditionRef
from netex.day_type_ref import DayTypeRef
from netex.fare_day_type_ref import FareDayTypeRef
from netex.group_of_timebands_ref import GroupOfTimebandsRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.operating_day_ref import OperatingDayRef
from netex.operating_period_ref import OperatingPeriodRef
from netex.uic_operating_period_ref import UicOperatingPeriodRef
from netex.validity_condition_ref import ValidityConditionRef
from netex.validity_rule_parameter_ref import ValidityRuleParameterRef
from netex.validity_trigger_ref import ValidityTriggerRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TemporalValidityParametersRelStructure(OneToManyRelationshipStructure):
    """
    One to many Relationship for temporal validity parameters.
    """
    class Meta:
        name = "temporalValidityParameters_RelStructure"

    fare_day_type_ref_or_day_type_ref: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareDayTypeRef",
                    "type": FareDayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DayTypeRef",
                    "type": DayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    group_of_timebands_ref: List[GroupOfTimebandsRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfTimebandsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    operating_day_ref: List[OperatingDayRef] = field(
        default_factory=list,
        metadata={
            "name": "OperatingDayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    uic_operating_period_ref_or_operating_period_ref: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "UicOperatingPeriodRef",
                    "type": UicOperatingPeriodRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatingPeriodRef",
                    "type": OperatingPeriodRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AvailabilityConditionRef",
                    "type": AvailabilityConditionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityRuleParameterRef",
                    "type": ValidityRuleParameterRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityTriggerRef",
                    "type": ValidityTriggerRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityConditionRef",
                    "type": ValidityConditionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
