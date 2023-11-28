from dataclasses import dataclass, field
from typing import List
from netex.availability_condition_ref import AvailabilityConditionRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.validity_condition_ref import ValidityConditionRef
from netex.validity_rule_parameter_ref import ValidityRuleParameterRef
from netex.validity_trigger_ref import ValidityTriggerRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ValidityConditionRefsRelStructure(OneToManyRelationshipStructure):
    """
    A collection of one or more VALIDITY CONDITIONs.
    """
    class Meta:
        name = "validityConditionRefs_RelStructure"

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
