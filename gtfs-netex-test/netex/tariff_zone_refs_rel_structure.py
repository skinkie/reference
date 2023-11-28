from dataclasses import dataclass, field
from typing import List
from netex.fare_zone_ref import FareZoneRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.tariff_zone_ref import TariffZoneRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TariffZoneRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of TARIFF ZONEs.
    """
    class Meta:
        name = "tariffZoneRefs_RelStructure"

    fare_zone_ref_or_tariff_zone_ref: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareZoneRef",
                    "type": FareZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TariffZoneRef",
                    "type": TariffZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
