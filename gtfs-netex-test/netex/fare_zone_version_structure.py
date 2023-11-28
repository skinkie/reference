from dataclasses import dataclass, field
from typing import Optional
from netex.authority_ref import AuthorityRef
from netex.fare_sections_rel_structure import FareSectionsRelStructure
from netex.fare_zone_ref_structure import FareZoneRefStructure
from netex.fare_zone_refs_rel_structure import FareZoneRefsRelStructure
from netex.group_of_operators_ref import GroupOfOperatorsRef
from netex.operator_ref import OperatorRef
from netex.scoping_method_enumeration import ScopingMethodEnumeration
from netex.tariff_zone_refs_rel_structure import TariffZoneRefsRelStructure
from netex.tariff_zone_version_structure import TariffZoneVersionStructure
from netex.zone_topology_enumeration import ZoneTopologyEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareZoneVersionStructure(TariffZoneVersionStructure):
    """
    Type for a FARE ZONE.

    :ivar parent_fare_zone_ref: Parent FARe ZONE that contains this
        ZONE.
    :ivar zone_topology: Classification of zone topology.
    :ivar scoping_method: Indication of how member stops of a FARE ZONE
        are specified (ExplicitStops, ImplicitSpatialProjection etc) .
        Default is ExplicitStops
    :ivar authority_ref_or_operator_ref:
    :ivar group_of_operators_ref:
    :ivar fare_sections: FARE SECTIONS in FARE ZONE.
    :ivar contains: Other fare zone that are wholly  included in the
        FARE ZONE.
    :ivar neighbours: Adjacent FARE ZONEs.
    """
    class Meta:
        name = "FareZone_VersionStructure"

    parent_fare_zone_ref: Optional[FareZoneRefStructure] = field(
        default=None,
        metadata={
            "name": "ParentFareZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    zone_topology: Optional[ZoneTopologyEnumeration] = field(
        default=None,
        metadata={
            "name": "ZoneTopology",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    scoping_method: Optional[ScopingMethodEnumeration] = field(
        default=None,
        metadata={
            "name": "ScopingMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    authority_ref_or_operator_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AuthorityRef",
                    "type": AuthorityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatorRef",
                    "type": OperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    group_of_operators_ref: Optional[GroupOfOperatorsRef] = field(
        default=None,
        metadata={
            "name": "GroupOfOperatorsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_sections: Optional[FareSectionsRelStructure] = field(
        default=None,
        metadata={
            "name": "fareSections",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    contains: Optional[TariffZoneRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    neighbours: Optional[FareZoneRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
