from dataclasses import dataclass, field
from typing import Optional
from netex.activated_equipments_in_frame_rel_structure import ActivatedEquipmentsInFrameRelStructure
from netex.activation_links_in_frame_rel_structure import ActivationLinksInFrameRelStructure
from netex.activation_points_in_frame_rel_structure import ActivationPointsInFrameRelStructure
from netex.common_version_frame_structure import CommonVersionFrameStructure
from netex.crew_bases_in_frame_rel_structure import CrewBasesInFrameRelStructure
from netex.garages_in_frame_rel_structure import GaragesInFrameRelStructure
from netex.infrastructure_elements_in_frame_rel_structure import InfrastructureElementsInFrameRelStructure
from netex.infrastructure_junctions_in_frame_rel_structure import InfrastructureJunctionsInFrameRelStructure
from netex.network_restrictions_in_frame_rel_structure import NetworkRestrictionsInFrameRelStructure
from netex.relief_points_in_frame_rel_structure import ReliefPointsInFrameRelStructure
from netex.spatial_features_in_frame_rel_structure import SpatialFeaturesInFrameRelStructure
from netex.traffic_control_points_in_frame_rel_structure import TrafficControlPointsInFrameRelStructure
from netex.vehicle_equipmen_profiles_in_frame_rel_structure import VehicleEquipmenProfilesInFrameRelStructure
from netex.vehicle_model_profiles_in_frame_rel_structure import VehicleModelProfilesInFrameRelStructure
from netex.vehicle_models_in_frame_rel_structure import VehicleModelsInFrameRelStructure
from netex.vehicle_types_in_frame_rel_structure import VehicleTypesInFrameRelStructure
from netex.vehicles_in_frame_rel_structure import VehiclesInFrameRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class InfrastructureVersionFrameStructure(CommonVersionFrameStructure):
    """
    Type for an INFRASTRUCTURE FRAME.

    :ivar meetings_restricted: Default sense for MEETING RESTRICTIONs in
        frame. If 'true', meetings at all points are restricted unless
        explicitly permittted,  If 'false', meetings at all points are
        allowed, unless explicitly forbidden by a MEETING RESTRICTION.
        Default is 'f'alse'.
    :ivar restricted_manoeuvres: Default sense for RESTRICTED MANOEUVRE
        in frame. If 'true', manoevres at all points are restricted
        unless explicitly permittted,  If 'false', meeting at all points
        is allowed, unless explicitly forbidden by a RESTRICTED
        MANOEUVRE. Default is 'f'alse'.
    :ivar overtaking_possibilities_restricted: Default sense for
        OVERTAKING POSSIBILITY restrictions in frame. If true,
        overtaking at all points is restricted unless explicitly
        permitted,  If 'false', meeting at all points is allowed, unless
        explicitly forbidden by an OVERTAKING POSSIBILITY. Default is
        'f'alse'.
    :ivar spatial_features: TARIFF ZONEs in frame.
    :ivar junctions: Junctions in Network in frame.
    :ivar elements: Elements (links) in Network in frame.
    :ivar restrictions: restrictions on network.
    :ivar crew_bases: Vehicle and CREW POINTs in frame.
    :ivar garages: Vehicle and CREW POINTs in frame.
    :ivar vehicle_and_crew_points: Vehicle and CREW POINTs in frame.
    :ivar traffic_control_points: points in frame.
    :ivar activation_points: points in frame.
    :ivar activation_links: links in frame.
    :ivar activated_equipments: equipment in frame.
    :ivar vehicle_types: VEHICLE TYPEs in frame.
    :ivar vehicle_models: VEHICLE MODELs in frame.
    :ivar vehicle_equipment_profiles: VEHICLE EQUIPMENT PROFILEs in
        frame.
    :ivar vehicle_model_profiles: VEHICLE MODEL PROFILEs in frame.
        +v1.2.2
    :ivar vehicles: VEHICLEs in frame.
    """
    class Meta:
        name = "Infrastructure_VersionFrameStructure"

    meetings_restricted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MeetingsRestricted",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    restricted_manoeuvres: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RestrictedManoeuvres",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    overtaking_possibilities_restricted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OvertakingPossibilitiesRestricted",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    spatial_features: Optional[SpatialFeaturesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "spatialFeatures",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    junctions: Optional[InfrastructureJunctionsInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    elements: Optional[InfrastructureElementsInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    restrictions: Optional[NetworkRestrictionsInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    crew_bases: Optional[CrewBasesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "crewBases",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    garages: Optional[GaragesInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_and_crew_points: Optional[ReliefPointsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "vehicleAndCrewPoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    traffic_control_points: Optional[TrafficControlPointsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "trafficControlPoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    activation_points: Optional[ActivationPointsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "activationPoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    activation_links: Optional[ActivationLinksInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "activationLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    activated_equipments: Optional[ActivatedEquipmentsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "activatedEquipments",
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
