from dataclasses import dataclass, field
from typing import Union

from .access_space_ref import AccessSpaceRef
from .address_ref import AddressRef
from .all_authorities_ref import AllAuthoritiesRef
from .all_modes_enumeration import AllModesEnumeration
from .all_operators_ref import AllOperatorsRef
from .all_organisations_ref import AllOrganisationsRef
from .all_public_transport_organisations_ref import AllPublicTransportOrganisationsRef
from .all_transport_organisations_ref import AllTransportOrganisationsRef
from .assistance_booking_service_ref import AssistanceBookingServiceRef
from .assistance_service_ref import AssistanceServiceRef
from .authority_ref import AuthorityRef
from .boarding_position_ref import BoardingPositionRef
from .border_point_ref import BorderPointRef
from .car_model_profile_ref import CarModelProfileRef
from .car_pooling_service_ref import CarPoolingServiceRef
from .catering_service_ref import CateringServiceRef
from .charging_moment_ref import ChargingMomentRef
from .chauffeured_vehicle_service_ref import ChauffeuredVehicleServiceRef
from .class_of_use_ref import ClassOfUseRef
from .communication_service_ref import CommunicationServiceRef
from .complaints_service_ref import ComplaintsServiceRef
from .compound_train_ref import CompoundTrainRef
from .customer_service_ref import CustomerServiceRef
from .cycle_model_profile_ref import CycleModelProfileRef
from .deck_plan_ref import DeckPlanRef
from .discounting_rule_ref import DiscountingRuleRef
from .distribution_channel_ref import DistributionChannelRef
from .entrance_ref import EntranceRef
from .facility_set_ref import FacilitySetRef
from .fare_class import FareClass
from .fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from .fare_section_ref import FareSectionRef
from .fare_zone_ref import FareZoneRef
from .flexible_line_ref import FlexibleLineRef
from .flexible_mode_of_operation_ref import FlexibleModeOfOperationRef
from .fulfilment_method_ref import FulfilmentMethodRef
from .general_organisation_ref import GeneralOrganisationRef
from .group_of_distribution_channels_ref import GroupOfDistributionChannelsRef
from .group_of_lines_ref import GroupOfLinesRef
from .group_of_operators_ref import GroupOfOperatorsRef
from .group_of_services_ref import GroupOfServicesRef
from .group_of_single_journeys_ref import GroupOfSingleJourneysRef
from .group_of_sites_ref import GroupOfSitesRef
from .group_of_tariff_zones_ref import GroupOfTariffZonesRef
from .hire_service_ref import HireServiceRef
from .left_luggage_service_ref import LeftLuggageServiceRef
from .level_ref import LevelRef
from .limiting_rule_ref import LimitingRuleRef
from .line_ref import LineRef
from .lost_property_service_ref import LostPropertyServiceRef
from .luggage_service_ref import LuggageServiceRef
from .luggage_spot_ref import LuggageSpotRef
from .management_agent_ref import ManagementAgentRef
from .meeting_point_service_ref import MeetingPointServiceRef
from .mobility_service_constraint_zone_ref import MobilityServiceConstraintZoneRef
from .money_service_ref import MoneyServiceRef
from .monitored_vehicle_sharing_parking_bay_ref import MonitoredVehicleSharingParkingBayRef
from .network_ref import NetworkRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .online_service_operator_ref import OnlineServiceOperatorRef
from .online_service_ref import OnlineServiceRef
from .operator_ref import OperatorRef
from .organisation_ref import OrganisationRef
from .other_deck_space_ref import OtherDeckSpaceRef
from .other_organisation_ref import OtherOrganisationRef
from .parking_area_ref import ParkingAreaRef
from .parking_bay_ref import ParkingBayRef
from .parking_entrance_for_vehicles_ref import ParkingEntranceForVehiclesRef
from .parking_entrance_ref import ParkingEntranceRef
from .parking_passenger_entrance_ref import ParkingPassengerEntranceRef
from .parking_ref import ParkingRef
from .parking_tariff_ref import ParkingTariffRef
from .passenger_seat_ref import PassengerSeatRef
from .passenger_space_ref import PassengerSpaceRef
from .passenger_spot_ref import PassengerSpotRef
from .passenger_vehicle_spot_ref import PassengerVehicleSpotRef
from .personal_mode_of_operation_ref import PersonalModeOfOperationRef
from .place_use_enumeration import PlaceUseEnumeration
from .point_of_interest_classification_ref import PointOfInterestClassificationRef
from .point_of_interest_entrance_ref import PointOfInterestEntranceRef
from .point_of_interest_ref import PointOfInterestRef
from .point_of_interest_space_ref import PointOfInterestSpaceRef
from .point_of_interest_vehicle_entrance_ref import PointOfInterestVehicleEntranceRef
from .postal_address_ref import PostalAddressRef
from .powered_train_ref import PoweredTrainRef
from .pricing_rule_ref import PricingRuleRef
from .quay_ref import QuayRef
from .relative_direction_enumeration import RelativeDirectionEnumeration
from .restricted_service_facility_set_ref import RestrictedServiceFacilitySetRef
from .retail_consortium_ref import RetailConsortiumRef
from .retail_service_ref import RetailServiceRef
from .road_address_ref import RoadAddressRef
from .routing_constraint_zone_ref import RoutingConstraintZoneRef
from .routing_type_enumeration import RoutingTypeEnumeration
from .scheduled_mode_of_operation_ref import ScheduledModeOfOperationRef
from .scheduled_stop_point_ref import ScheduledStopPointRef
from .series_constraint_ref import SeriesConstraintRef
from .service_exclusion_ref import ServiceExclusionRef
from .service_facility_set_ref import ServiceFacilitySetRef
from .service_journey_pattern_ref import ServiceJourneyPatternRef
from .service_journey_ref import ServiceJourneyRef
from .service_site_ref import ServiceSiteRef
from .serviced_organisation_ref import ServicedOrganisationRef
from .simple_vehicle_type_ref import SimpleVehicleTypeRef
from .single_journey_path_ref import SingleJourneyPathRef
from .single_journey_ref import SingleJourneyRef
from .site_component_ref import SiteComponentRef
from .site_element_ref import SiteElementRef
from .site_facility_set_ref import SiteFacilitySetRef
from .site_ref import SiteRef
from .spot_column_ref import SpotColumnRef
from .spot_row_ref import SpotRowRef
from .stop_place_entrance_ref import StopPlaceEntranceRef
from .stop_place_ref import StopPlaceRef
from .stop_place_space_ref import StopPlaceSpaceRef
from .stop_place_vehicle_entrance_ref import StopPlaceVehicleEntranceRef
from .tariff_ref import TariffRef
from .tariff_zone_ref import TariffZoneRef
from .taxi_parking_area_ref import TaxiParkingAreaRef
from .taxi_rank_ref import TaxiRankRef
from .taxi_service_ref import TaxiServiceRef
from .taxi_stand_ref import TaxiStandRef
from .template_service_journey_ref import TemplateServiceJourneyRef
from .ticketing_service_ref import TicketingServiceRef
from .topographic_place_ref import TopographicPlaceRef
from .train_component_label_assignment_ref import TrainComponentLabelAssignmentRef
from .train_element_ref import TrainElementRef
from .train_number_ref import TrainNumberRef
from .train_ref import TrainRef
from .transfer_restriction_ref import TransferRestrictionRef
from .transport_submode import TransportSubmode
from .transport_type_ref import TransportTypeRef
from .travel_agent_ref import TravelAgentRef
from .type_of_concession_ref import TypeOfConcessionRef
from .type_of_fare_product_ref import TypeOfFareProductRef
from .type_of_fare_structure_element_ref import TypeOfFareStructureElementRef
from .type_of_fare_structure_factor_ref import TypeOfFareStructureFactorRef
from .type_of_line_ref import TypeOfLineRef
from .type_of_locatable_spot_ref import TypeOfLocatableSpotRef
from .type_of_machine_readability_ref import TypeOfMachineReadabilityRef
from .type_of_medium_access_device_ref import TypeOfMediumAccessDeviceRef
from .type_of_payment_method_ref import TypeOfPaymentMethodRef
from .type_of_pricing_rule_ref import TypeOfPricingRuleRef
from .type_of_product_category_ref import TypeOfProductCategoryRef
from .type_of_proof_ref import TypeOfProofRef
from .type_of_sales_offer_package_ref import TypeOfSalesOfferPackageRef
from .type_of_service_ref import TypeOfServiceRef
from .type_of_tariff_ref import TypeOfTariffRef
from .type_of_travel_document_ref import TypeOfTravelDocumentRef
from .type_of_usage_parameter_ref import TypeOfUsageParameterRef
from .types_of_proof_refs_rel_structure import TypesOfProofRefsRelStructure
from .unpowered_train_ref import UnpoweredTrainRef
from .vehicle_entrance_ref import VehicleEntranceRef
from .vehicle_meeting_link_ref import VehicleMeetingLinkRef
from .vehicle_meeting_place_ref import VehicleMeetingPlaceRef
from .vehicle_meeting_point_ref import VehicleMeetingPointRef
from .vehicle_mode_enumeration import VehicleModeEnumeration
from .vehicle_model_ref import VehicleModelRef
from .vehicle_pooling_meeting_place_ref import VehiclePoolingMeetingPlaceRef
from .vehicle_pooling_parking_area_ref import VehiclePoolingParkingAreaRef
from .vehicle_pooling_parking_bay_ref import VehiclePoolingParkingBayRef
from .vehicle_pooling_ref import VehiclePoolingRef
from .vehicle_ref import VehicleRef
from .vehicle_rental_ref import VehicleRentalRef
from .vehicle_rental_service_ref import VehicleRentalServiceRef
from .vehicle_sharing_parking_area_ref import VehicleSharingParkingAreaRef
from .vehicle_sharing_parking_bay_ref import VehicleSharingParkingBayRef
from .vehicle_sharing_ref import VehicleSharingRef
from .vehicle_sharing_service_ref import VehicleSharingServiceRef
from .vehicle_stopping_place_ref import VehicleStoppingPlaceRef
from .vehicle_stopping_position_ref import VehicleStoppingPositionRef
from .vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ValidityParametersRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "validityParameters_RelStructure"

    vehicle_modes_or_transport_modes: list[Union[list[VehicleModeEnumeration], list[AllModesEnumeration]]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleModes",
                    "type": list[VehicleModeEnumeration],
                    "namespace": "http://www.netex.org.uk/netex",
                    "default_factory": list,
                    "tokens": True,
                },
                {
                    "name": "TransportModes",
                    "type": list[AllModesEnumeration],
                    "namespace": "http://www.netex.org.uk/netex",
                    "default_factory": list,
                    "tokens": True,
                },
            ),
        },
    )
    transport_submode: list[TransportSubmode] = field(
        default_factory=list,
        metadata={
            "name": "TransportSubmode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    mode_of_operation_ref_or_alternative_mode_of_operation_ref_or_conventional_mode_of_operation_ref: list[Union[PersonalModeOfOperationRef, VehiclePoolingRef, VehicleSharingRef, VehicleRentalRef, FlexibleModeOfOperationRef, ScheduledModeOfOperationRef]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PersonalModeOfOperationRef",
                    "type": PersonalModeOfOperationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePoolingRef",
                    "type": VehiclePoolingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingRef",
                    "type": VehicleSharingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleRentalRef",
                    "type": VehicleRentalRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleModeOfOperationRef",
                    "type": FlexibleModeOfOperationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledModeOfOperationRef",
                    "type": ScheduledModeOfOperationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    group_of_operators_ref: list[GroupOfOperatorsRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfOperatorsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    all_public_transport_organisations_ref_or_all_transport_organisations_ref_or_all_organisations_ref_or_organisation_ref_or_other_organisation_ref_or_transport_organisation_ref: list[
        Union[
            AllAuthoritiesRef,
            AllOperatorsRef,
            AllPublicTransportOrganisationsRef,
            AllTransportOrganisationsRef,
            AllOrganisationsRef,
            RetailConsortiumRef,
            OnlineServiceOperatorRef,
            GeneralOrganisationRef,
            ManagementAgentRef,
            ServicedOrganisationRef,
            TravelAgentRef,
            OtherOrganisationRef,
            AuthorityRef,
            OperatorRef,
            OrganisationRef,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AllAuthoritiesRef",
                    "type": AllAuthoritiesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AllOperatorsRef",
                    "type": AllOperatorsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AllPublicTransportOrganisationsRef",
                    "type": AllPublicTransportOrganisationsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AllTransportOrganisationsRef",
                    "type": AllTransportOrganisationsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AllOrganisationsRef",
                    "type": AllOrganisationsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
        },
    )
    group_of_lines_ref: list[Union[NetworkRef, GroupOfLinesRef]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "NetworkRef",
                    "type": NetworkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfLinesRef",
                    "type": GroupOfLinesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    line_ref: list[Union[FlexibleLineRef, LineRef]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleLineRef",
                    "type": FlexibleLineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineRef",
                    "type": LineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    type_of_line_ref: list[TypeOfLineRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfLineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    group_of_tariff_zones_ref: list[GroupOfTariffZonesRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfTariffZonesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    tariff_zone_ref: list[TariffZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "TariffZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    fare_zone_ref: list[FareZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "FareZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    fare_section_ref: list[FareSectionRef] = field(
        default_factory=list,
        metadata={
            "name": "FareSectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    scheduled_stop_point_ref: list[Union[FareScheduledStopPointRef, ScheduledStopPointRef]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareScheduledStopPointRef",
                    "type": FareScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledStopPointRef",
                    "type": ScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    vehicle_meeting_point_ref: list[VehicleMeetingPointRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleMeetingPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    vehicle_meeting_link_ref: list[VehicleMeetingLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleMeetingLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    vehicle_meeting_place_ref: list[Union[VehiclePoolingMeetingPlaceRef, VehicleMeetingPlaceRef]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehiclePoolingMeetingPlaceRef",
                    "type": VehiclePoolingMeetingPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleMeetingPlaceRef",
                    "type": VehicleMeetingPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    place_use: list[PlaceUseEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PlaceUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    topographic_place_ref: list[TopographicPlaceRef] = field(
        default_factory=list,
        metadata={
            "name": "TopographicPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    address_ref: list[Union[PostalAddressRef, RoadAddressRef, AddressRef]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PostalAddressRef",
                    "type": PostalAddressRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadAddressRef",
                    "type": RoadAddressRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AddressRef",
                    "type": AddressRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    group_of_sites_ref: list[GroupOfSitesRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfSitesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    choice: list[
        Union[
            VehicleStoppingPositionRef,
            VehicleStoppingPlaceRef,
            VehiclePoolingParkingBayRef,
            MonitoredVehicleSharingParkingBayRef,
            VehicleSharingParkingBayRef,
            ParkingBayRef,
            VehiclePoolingParkingAreaRef,
            VehicleSharingParkingAreaRef,
            TaxiParkingAreaRef,
            ParkingAreaRef,
            PointOfInterestSpaceRef,
            BoardingPositionRef,
            AccessSpaceRef,
            TaxiStandRef,
            QuayRef,
            StopPlaceSpaceRef,
            ParkingEntranceForVehiclesRef,
            ParkingPassengerEntranceRef,
            ParkingEntranceRef,
            PointOfInterestVehicleEntranceRef,
            PointOfInterestEntranceRef,
            StopPlaceVehicleEntranceRef,
            StopPlaceEntranceRef,
            VehicleEntranceRef,
            EntranceRef,
            SiteComponentRef,
            ParkingRef,
            PointOfInterestRef,
            TaxiRankRef,
            StopPlaceRef,
            ServiceSiteRef,
            SiteRef,
            SiteElementRef,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleStoppingPositionRef",
                    "type": VehicleStoppingPositionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleStoppingPlaceRef",
                    "type": VehicleStoppingPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePoolingParkingBayRef",
                    "type": VehiclePoolingParkingBayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MonitoredVehicleSharingParkingBayRef",
                    "type": MonitoredVehicleSharingParkingBayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingParkingBayRef",
                    "type": VehicleSharingParkingBayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingBayRef",
                    "type": ParkingBayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePoolingParkingAreaRef",
                    "type": VehiclePoolingParkingAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingParkingAreaRef",
                    "type": VehicleSharingParkingAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiParkingAreaRef",
                    "type": TaxiParkingAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingAreaRef",
                    "type": ParkingAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestSpaceRef",
                    "type": PointOfInterestSpaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BoardingPositionRef",
                    "type": BoardingPositionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessSpaceRef",
                    "type": AccessSpaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiStandRef",
                    "type": TaxiStandRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QuayRef",
                    "type": QuayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlaceSpaceRef",
                    "type": StopPlaceSpaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingEntranceForVehiclesRef",
                    "type": ParkingEntranceForVehiclesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPassengerEntranceRef",
                    "type": ParkingPassengerEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingEntranceRef",
                    "type": ParkingEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestVehicleEntranceRef",
                    "type": PointOfInterestVehicleEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestEntranceRef",
                    "type": PointOfInterestEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlaceVehicleEntranceRef",
                    "type": StopPlaceVehicleEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlaceEntranceRef",
                    "type": StopPlaceEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleEntranceRef",
                    "type": VehicleEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntranceRef",
                    "type": EntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteComponentRef",
                    "type": SiteComponentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingRef",
                    "type": ParkingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestRef",
                    "type": PointOfInterestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiRankRef",
                    "type": TaxiRankRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlaceRef",
                    "type": StopPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceSiteRef",
                    "type": ServiceSiteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteRef",
                    "type": SiteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteElementRef",
                    "type": SiteElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    level_ref: list[LevelRef] = field(
        default_factory=list,
        metadata={
            "name": "LevelRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    point_of_interest_classification_ref: list[PointOfInterestClassificationRef] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestClassificationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    mobility_service_constraint_zone_ref: list[MobilityServiceConstraintZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "MobilityServiceConstraintZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    routing_type: list[RoutingTypeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "RoutingType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    directions: list[RelativeDirectionEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "Directions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    border_point_ref: list[BorderPointRef] = field(
        default_factory=list,
        metadata={
            "name": "BorderPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    series_constraint_ref: list[SeriesConstraintRef] = field(
        default_factory=list,
        metadata={
            "name": "SeriesConstraintRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    service_journey_pattern_ref: list[ServiceJourneyPatternRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    single_journey_path_ref: list[SingleJourneyPathRef] = field(
        default_factory=list,
        metadata={
            "name": "SingleJourneyPathRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    transfer_restriction_ref: list[TransferRestrictionRef] = field(
        default_factory=list,
        metadata={
            "name": "TransferRestrictionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    routing_constraint_zone_ref: list[RoutingConstraintZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "RoutingConstraintZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    service_exclusion_ref: list[ServiceExclusionRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceExclusionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    class_of_use_ref: list[ClassOfUseRef] = field(
        default_factory=list,
        metadata={
            "name": "ClassOfUseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    fare_class: list[FareClass] = field(
        default_factory=list,
        metadata={
            "name": "FareClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    service_facility_set_ref_or_facility_set_ref: list[Union[RestrictedServiceFacilitySetRef, ServiceFacilitySetRef, SiteFacilitySetRef, FacilitySetRef]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RestrictedServiceFacilitySetRef",
                    "type": RestrictedServiceFacilitySetRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceFacilitySetRef",
                    "type": ServiceFacilitySetRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteFacilitySetRef",
                    "type": SiteFacilitySetRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FacilitySetRef",
                    "type": FacilitySetRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    type_of_product_category_ref: list[TypeOfProductCategoryRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfProductCategoryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    service_journey_ref: list[Union[TemplateServiceJourneyRef, ServiceJourneyRef]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TemplateServiceJourneyRef",
                    "type": TemplateServiceJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyRef",
                    "type": ServiceJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    train_number_ref: list[TrainNumberRef] = field(
        default_factory=list,
        metadata={
            "name": "TrainNumberRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    group_of_services_ref: list[GroupOfServicesRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfServicesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    single_journey_ref: list[SingleJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "SingleJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    group_of_single_journeys_ref: list[GroupOfSingleJourneysRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfSingleJourneysRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    transport_type_ref_or_vehicle_type_ref_or_train_ref: list[Union[SimpleVehicleTypeRef, CompoundTrainRef, UnpoweredTrainRef, PoweredTrainRef, TrainRef, VehicleTypeRef, TransportTypeRef]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SimpleVehicleTypeRef",
                    "type": SimpleVehicleTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompoundTrainRef",
                    "type": CompoundTrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UnpoweredTrainRef",
                    "type": UnpoweredTrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PoweredTrainRef",
                    "type": PoweredTrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainRef",
                    "type": TrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleTypeRef",
                    "type": VehicleTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransportTypeRef",
                    "type": TransportTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    vehicle_model_ref: list[VehicleModelRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleModelRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    type_of_service_ref: list[TypeOfServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    vehicle_model_profile_ref: list[Union[CycleModelProfileRef, CarModelProfileRef]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CycleModelProfileRef",
                    "type": CycleModelProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CarModelProfileRef",
                    "type": CarModelProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    mobility_service_ref_or_common_vehicle_service_ref_or_vehicle_pooling_service_ref_or_local_service_ref: list[
        Union[
            OnlineServiceRef,
            VehicleRentalServiceRef,
            VehicleSharingServiceRef,
            ChauffeuredVehicleServiceRef,
            TaxiServiceRef,
            CarPoolingServiceRef,
            AssistanceBookingServiceRef,
            CateringServiceRef,
            RetailServiceRef,
            MoneyServiceRef,
            HireServiceRef,
            CommunicationServiceRef,
            MeetingPointServiceRef,
            LeftLuggageServiceRef,
            LuggageServiceRef,
            LostPropertyServiceRef,
            ComplaintsServiceRef,
            CustomerServiceRef,
            AssistanceServiceRef,
            TicketingServiceRef,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OnlineServiceRef",
                    "type": OnlineServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleRentalServiceRef",
                    "type": VehicleRentalServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingServiceRef",
                    "type": VehicleSharingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChauffeuredVehicleServiceRef",
                    "type": ChauffeuredVehicleServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiServiceRef",
                    "type": TaxiServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CarPoolingServiceRef",
                    "type": CarPoolingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AssistanceBookingServiceRef",
                    "type": AssistanceBookingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CateringServiceRef",
                    "type": CateringServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RetailServiceRef",
                    "type": RetailServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MoneyServiceRef",
                    "type": MoneyServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HireServiceRef",
                    "type": HireServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommunicationServiceRef",
                    "type": CommunicationServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MeetingPointServiceRef",
                    "type": MeetingPointServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LeftLuggageServiceRef",
                    "type": LeftLuggageServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LuggageServiceRef",
                    "type": LuggageServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LostPropertyServiceRef",
                    "type": LostPropertyServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ComplaintsServiceRef",
                    "type": ComplaintsServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerServiceRef",
                    "type": CustomerServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AssistanceServiceRef",
                    "type": AssistanceServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TicketingServiceRef",
                    "type": TicketingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    train_element_ref: list[TrainElementRef] = field(
        default_factory=list,
        metadata={
            "name": "TrainElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    train_component_label_assignment_ref: list[TrainComponentLabelAssignmentRef] = field(
        default_factory=list,
        metadata={
            "name": "TrainComponentLabelAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    deck_plan_ref: list[DeckPlanRef] = field(
        default_factory=list,
        metadata={
            "name": "DeckPlanRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    deck_space_ref: list[Union[OtherDeckSpaceRef, PassengerSpaceRef]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OtherDeckSpaceRef",
                    "type": OtherDeckSpaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerSpaceRef",
                    "type": PassengerSpaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    spot_column_ref: list[SpotColumnRef] = field(
        default_factory=list,
        metadata={
            "name": "SpotColumnRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    spot_row_ref: list[SpotRowRef] = field(
        default_factory=list,
        metadata={
            "name": "SpotRowRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    locatable_spot_ref: list[Union[LuggageSpotRef, PassengerVehicleSpotRef, PassengerSpotRef]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "LuggageSpotRef",
                    "type": LuggageSpotRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerVehicleSpotRef",
                    "type": PassengerVehicleSpotRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerSpotRef",
                    "type": PassengerSpotRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    type_of_locatable_spot_ref: list[TypeOfLocatableSpotRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfLocatableSpotRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    passenger_seat_ref: list[PassengerSeatRef] = field(
        default_factory=list,
        metadata={
            "name": "PassengerSeatRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    vehicle_ref: list[VehicleRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    type_of_fare_structure_factor_ref: list[TypeOfFareStructureFactorRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareStructureFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    type_of_fare_structure_element_ref: list[TypeOfFareStructureElementRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareStructureElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    type_of_tariff_ref: list[TypeOfTariffRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfTariffRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    tariff_ref: list[Union[ParkingTariffRef, TariffRef]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ParkingTariffRef",
                    "type": ParkingTariffRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TariffRef",
                    "type": TariffRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    discounting_rule_ref_or_pricing_rule_ref: list[Union[LimitingRuleRef, DiscountingRuleRef, PricingRuleRef]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "LimitingRuleRef",
                    "type": LimitingRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DiscountingRuleRef",
                    "type": DiscountingRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PricingRuleRef",
                    "type": PricingRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    type_of_pricing_rule_ref: list[TypeOfPricingRuleRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPricingRuleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    charging_moment_ref: list[ChargingMomentRef] = field(
        default_factory=list,
        metadata={
            "name": "ChargingMomentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    type_of_fare_product_ref: list[TypeOfFareProductRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    type_of_usage_parameter_ref: list[TypeOfUsageParameterRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfUsageParameterRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    type_of_concession_ref: list[TypeOfConcessionRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfConcessionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    type_of_proof_ref: list[TypeOfProofRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfProofRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    types_of_proof_accepted_ref: list[TypesOfProofRefsRelStructure] = field(
        default_factory=list,
        metadata={
            "name": "typesOfProofAcceptedRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    type_of_sales_offer_package_ref: list[TypeOfSalesOfferPackageRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfSalesOfferPackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    type_of_travel_document_ref: list[TypeOfTravelDocumentRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfTravelDocumentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    type_of_machine_readability_ref: list[TypeOfMachineReadabilityRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfMachineReadabilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    type_of_medium_access_device_ref: list[TypeOfMediumAccessDeviceRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfMediumAccessDeviceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    distribution_channel_ref_or_group_of_distribution_channels_ref: list[Union[DistributionChannelRef, GroupOfDistributionChannelsRef]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DistributionChannelRef",
                    "type": DistributionChannelRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfDistributionChannelsRef",
                    "type": GroupOfDistributionChannelsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    fulfilment_method_ref: list[FulfilmentMethodRef] = field(
        default_factory=list,
        metadata={
            "name": "FulfilmentMethodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
    type_of_payment_method_ref: list[TypeOfPaymentMethodRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPaymentMethodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        },
    )
