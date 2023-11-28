from dataclasses import dataclass, field
from typing import List, Optional
from netex.administrative_zone_ref import AdministrativeZoneRef
from netex.all_modes_enumeration import AllModesEnumeration
from netex.authority_ref import AuthorityRef
from netex.codespace_assignments_rel_structure import CodespaceAssignmentsRelStructure
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.general_organisation_ref import GeneralOrganisationRef
from netex.management_agent_ref import ManagementAgentRef
from netex.online_service_operator_ref import OnlineServiceOperatorRef
from netex.operator_ref import OperatorRef
from netex.organisation_ref import OrganisationRef
from netex.other_organisation_ref import OtherOrganisationRef
from netex.private_code_structure import PrivateCodeStructure
from netex.responsibility_sets_rel_structure import ResponsibilitySetsRelStructure
from netex.retail_consortium_ref import RetailConsortiumRef
from netex.serviced_organisation_ref import ServicedOrganisationRef
from netex.travel_agent_ref import TravelAgentRef
from netex.zone_version_structure import ZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AdministrativeZoneVersionStructure(ZoneVersionStructure):
    """
    Type for an ADMINISTRATIVE ZONE.

    :ivar public_code: Public Code assosociated with Zone
    :ivar choice:
    :ivar responsibilities: RESPONSIBILITY SETs allocated to
        ADMINISTRATIVE ZONE.
    :ivar codespace_assignments: CODESPACEs belonging to ADMINISTRATIVE
        ZONE.
    :ivar subzones: Subzones of  ADMINISTRATIVE Zone; ie. strict
        subzones that are administrative subdivisions of the parent.
        These should not contradict Parent ZONE references..
    """
    class Meta:
        name = "AdministrativeZone_VersionStructure"

    public_code: Optional[PrivateCodeStructure] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    choice: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RetailConsortiumRef",
                    "type": RetailConsortiumRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OnlineServiceOperatorRef",
                    "type": OnlineServiceOperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralOrganisationRef",
                    "type": GeneralOrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ManagementAgentRef",
                    "type": ManagementAgentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServicedOrganisationRef",
                    "type": ServicedOrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelAgentRef",
                    "type": TravelAgentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OtherOrganisationRef",
                    "type": OtherOrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "OrganisationRef",
                    "type": OrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    responsibilities: Optional[ResponsibilitySetsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    codespace_assignments: Optional[CodespaceAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "codespaceAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    subzones: Optional["AdministrativeZonesRelStructure"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class AdministrativeZone(AdministrativeZoneVersionStructure):
    """A ZONE relating to the management responsibilities of an ORGANISATION.

    For example to allocate bus stop identifiers for a region.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class TransportAdministrativeZoneVersionStructure(AdministrativeZoneVersionStructure):
    """
    Type for an TRANSPORT ADMINISTRATIVE  ZONE.

    :ivar vehicle_modes: TRANSPORT MODEs for which this zone applies.
        Default is all.
    """
    class Meta:
        name = "TransportAdministrativeZone_VersionStructure"

    vehicle_modes: List[AllModesEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "VehicleModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class TransportAdministrativeZone(TransportAdministrativeZoneVersionStructure):
    """A ZONE relating to the management responsibilities of an ORGANISATION.

    For example to allocate bus stop identifiers for a region.

    :ivar id: Identifier of TRANSPORT ADMINISTRATIVE ZONE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class AdministrativeZonesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of ADMINISTRATIVE ZONEs.
    """
    class Meta:
        name = "administrativeZones_RelStructure"

    administrative_zone_ref_or_transport_administrative_zone_or_administrative_zone: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AdministrativeZoneRef",
                    "type": AdministrativeZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransportAdministrativeZone",
                    "type": TransportAdministrativeZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AdministrativeZone",
                    "type": AdministrativeZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
