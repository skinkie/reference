from dataclasses import dataclass, field
from typing import Optional
from netex.authority_ref import AuthorityRef
from netex.group_of_lines_version_structure import GroupOfLinesVersionStructure
from netex.groups_of_lines_in_frame_rel_structure import GroupsOfLinesInFrameRelStructure
from netex.groups_of_operators_refs_rel_structure import GroupsOfOperatorsRefsRelStructure
from netex.operator_ref import OperatorRef
from netex.tariff_zone_refs_rel_structure import TariffZoneRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class NetworkVersionStructure(GroupOfLinesVersionStructure):
    """
    Type for a NETWORK.

    :ivar authority_ref_or_operator_ref:
    :ivar groups_of_operators: Groups of OPERATORs  AUTHORTies or
        OPERATORS) (in NETWORK.
    :ivar groups_of_lines: Groups of LINEs in NETWORK.
    :ivar tariff_zones: TARIFF ZONEs in NETWORK.
    """
    class Meta:
        name = "Network_VersionStructure"

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
    groups_of_operators: Optional[GroupsOfOperatorsRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "groupsOfOperators",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    groups_of_lines: Optional[GroupsOfLinesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "groupsOfLines",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tariff_zones: Optional[TariffZoneRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "tariffZones",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
