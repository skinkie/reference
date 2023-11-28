from dataclasses import dataclass, field
from typing import List
from netex.flexible_service_properties import FlexibleServiceProperties
from netex.flexible_service_properties_ref import FlexibleServicePropertiesRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FlexibleServicePropertiesRelStructure(OneToManyRelationshipStructure):
    """
    Type for containment in frame of FLEXIBLE SERVICE PROPERTies.
    """
    class Meta:
        name = "flexibleServiceProperties_RelStructure"

    flexible_service_properties_ref_or_flexible_service_properties: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleServicePropertiesRef",
                    "type": FlexibleServicePropertiesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleServiceProperties",
                    "type": FlexibleServiceProperties,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
