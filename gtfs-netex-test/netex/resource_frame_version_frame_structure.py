from dataclasses import dataclass, field
from typing import Optional
from netex.blacklists_in_frame_rel_structure import BlacklistsInFrameRelStructure
from netex.common_version_frame_structure import CommonVersionFrameStructure
from netex.contacts_rel_structure import ContactsRelStructure
from netex.control_centres_in_frame_rel_structure import ControlCentresInFrameRelStructure
from netex.data_sources_in_frame_rel_structure import DataSourcesInFrameRelStructure
from netex.equipments_in_frame_rel_structure import EquipmentsInFrameRelStructure
from netex.group_of_entities_in_frame_rel_structure import GroupOfEntitiesInFrameRelStructure
from netex.groups_of_operators_in_frame_rel_structure import GroupsOfOperatorsInFrameRelStructure
from netex.modes_of_operation_rel_structure import ModesOfOperationRelStructure
from netex.open_modes_rel_structure import OpenModesRelStructure
from netex.operational_contexts_in_frame_rel_structure import OperationalContextsInFrameRelStructure
from netex.organisations_in_frame_rel_structure import OrganisationsInFrameRelStructure
from netex.responsibility_roles_in_frame_rel_structure import ResponsibilityRolesInFrameRelStructure
from netex.responsibility_sets_in_frame_rel_structure import ResponsibilitySetsInFrameRelStructure
from netex.schematic_maps_in_frame_rel_structure import SchematicMapsInFrameRelStructure
from netex.service_facility_sets_in_frame_rel_structure import ServiceFacilitySetsInFrameRelStructure
from netex.site_facility_sets_in_frame_rel_structure import SiteFacilitySetsInFrameRelStructure
from netex.types_of_value_in_frame_rel_structure import TypesOfValueInFrameRelStructure
from netex.vehicle_equipmen_profiles_in_frame_rel_structure import VehicleEquipmenProfilesInFrameRelStructure
from netex.vehicle_model_profiles_in_frame_rel_structure import VehicleModelProfilesInFrameRelStructure
from netex.vehicle_models_in_frame_rel_structure import VehicleModelsInFrameRelStructure
from netex.vehicle_types_in_frame_rel_structure import VehicleTypesInFrameRelStructure
from netex.vehicles_in_frame_rel_structure import VehiclesInFrameRelStructure
from netex.whitelists_in_frame_rel_structure import WhitelistsInFrameRelStructure
from netex.zones_in_frame_rel_structure import ZonesInFrameRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ResourceFrameVersionFrameStructure(CommonVersionFrameStructure):
    """
    Type for a RESOURCE.

    :ivar data_sources: Definitions of DATA SOURCE included in frame.
    :ivar responsibility_roles: RESPONSIBILITY Roles used in frame.
    :ivar responsibility_sets: RESPONSIBILITY SETs used in frame.
    :ivar types_of_value: VALUE SETs and  TYPE OF VALUEs in frame.
    :ivar contacts: Reusable CONTACTs in frame.
    :ivar organisations: ORGANISATIONs in frame.
    :ivar groups_of_operators: GROUPs OF OPERATORs in frame.
    :ivar operational_contexts: OPERATIONAL CONTEXTs in frame.
    :ivar control_centres: CONTROL CENTREs in frame.
    :ivar open_modes: OPEN MODES in FRAME
    :ivar modes_of_operation: MODES OF OPERATION in frame.
    :ivar equipments: EQUIPMENTs in frame.
    :ivar site_facility_sets: SITE FACILITY SETs in frame . +v1.2.2
    :ivar service_facility_sets: SERVICE FACILITY SETs in frame .
        +v1.2.2
    :ivar vehicle_types: VEHICLE TYPEs in frame.
    :ivar vehicle_models: VEHICLE MODELs in frame.
    :ivar vehicle_equipment_profiles: VEHICLE EQUIPMENT PROFILEs in
        frame.
    :ivar vehicle_model_profiles: VEHICLE MODEL PROFILEs in frame.
        +v1.2.2
    :ivar vehicles: VEHICLEs in frame.
    :ivar schematic_maps: SCHEMATIC MAP in frame.
    :ivar groups_of_entities: GROUPs of ENTITIEs in frame.
    :ivar zones: ZONEs in FRAME
    :ivar blacklists: BLACK LISTs in FRAME.
    :ivar whitelists: WHITE LISTs in FRAME.
    """
    class Meta:
        name = "ResourceFrame_VersionFrameStructure"

    data_sources: Optional[DataSourcesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "dataSources",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    responsibility_roles: Optional[ResponsibilityRolesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "responsibilityRoles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    responsibility_sets: Optional[ResponsibilitySetsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "responsibilitySets",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    types_of_value: Optional[TypesOfValueInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "typesOfValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    contacts: Optional[ContactsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    organisations: Optional[OrganisationsInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    groups_of_operators: Optional[GroupsOfOperatorsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "groupsOfOperators",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operational_contexts: Optional[OperationalContextsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "operationalContexts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    control_centres: Optional[ControlCentresInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "controlCentres",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    open_modes: Optional[OpenModesRelStructure] = field(
        default=None,
        metadata={
            "name": "openModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    modes_of_operation: Optional[ModesOfOperationRelStructure] = field(
        default=None,
        metadata={
            "name": "modesOfOperation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    equipments: Optional[EquipmentsInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    site_facility_sets: Optional[SiteFacilitySetsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "siteFacilitySets",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_facility_sets: Optional[ServiceFacilitySetsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "serviceFacilitySets",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_types: Optional[VehicleTypesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "vehicleTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_models: Optional[VehicleModelsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "vehicleModels",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_equipment_profiles: Optional[VehicleEquipmenProfilesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "vehicleEquipmentProfiles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_model_profiles: Optional[VehicleModelProfilesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "vehicleModelProfiles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicles: Optional[VehiclesInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    schematic_maps: Optional[SchematicMapsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "schematicMaps",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    groups_of_entities: Optional[GroupOfEntitiesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "groupsOfEntities",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    zones: Optional[ZonesInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    blacklists: Optional[BlacklistsInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    whitelists: Optional[WhitelistsInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
