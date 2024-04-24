from dataclasses import dataclass, field
from typing import List

from .group_of_tariff_zones_ref import GroupOfTariffZonesRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfTariffZoneRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "groupOfTariffZoneRefs_RelStructure"

    group_of_tariff_zones_ref: List[GroupOfTariffZonesRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfTariffZonesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
