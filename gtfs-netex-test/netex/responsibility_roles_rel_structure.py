from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.responsibility_role_ref import ResponsibilityRoleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ResponsibilityRolesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of RESPONSIBILITY ROLEs.
    """
    class Meta:
        name = "ResponsibilityRoles_RelStructure"

    responsibility_role_ref: List[ResponsibilityRoleRef] = field(
        default_factory=list,
        metadata={
            "name": "ResponsibilityRoleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
