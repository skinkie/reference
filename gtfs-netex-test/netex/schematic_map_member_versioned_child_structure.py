from dataclasses import dataclass, field
from typing import Optional, Union

from .accepted_driver_permit_ref import AcceptedDriverPermitRef
from .access_ref import AccessRef
from .access_right_in_product_ref import AccessRightInProductRef
from .access_space_ref import AccessSpaceRef
from .access_zone_ref import AccessZoneRef
from .accommodation_ref import AccommodationRef
from .accountable_element_ref import AccountableElementRef
from .activation_link_ref import ActivationLinkRef
from .activation_point_ref import ActivationPointRef
from .additional_driver_option_ref import AdditionalDriverOptionRef
from .address_ref import AddressRef
from .addressable_place_ref import AddressablePlaceRef
from .administrative_zone_ref import AdministrativeZoneRef
from .all_authorities_ref import AllAuthoritiesRef
from .all_distribution_channels_ref import AllDistributionChannelsRef
from .all_operators_ref import AllOperatorsRef
from .all_organisations_ref import AllOrganisationsRef
from .all_public_transport_organisations_ref import AllPublicTransportOrganisationsRef
from .all_transport_organisations_ref import AllTransportOrganisationsRef
from .allowed_line_direction_ref import AllowedLineDirectionRef
from .alternative_name_ref import AlternativeNameRef
from .alternative_text_ref import AlternativeTextRef
from .amount_of_price_unit_product_ref import AmountOfPriceUnitProductRef
from .authority_ref import AuthorityRef
from .availability_condition_ref import AvailabilityConditionRef
from .beacon_point_ref import BeaconPointRef
from .blacklist_ref import BlacklistRef
from .block_part_ref import BlockPartRef
from .block_ref import BlockRef
from .boarding_position_ref import BoardingPositionRef
from .booking_debit_ref import BookingDebitRef
from .booking_policy_ref import BookingPolicyRef
from .border_point_ref import BorderPointRef
from .branding_ref import BrandingRef
from .cancelling_ref import CancellingRef
from .capped_discount_right_ref import CappedDiscountRightRef
from .capping_rule_price_ref import CappingRulePriceRef
from .capping_rule_ref import CappingRuleRef
from .car_model_profile_ref import CarModelProfileRef
from .cell_ref import CellRef
from .charging_moment_ref import ChargingMomentRef
from .charging_policy_ref import ChargingPolicyRef
from .class_of_use_ref import ClassOfUseRef
from .commercial_profile_eligibility_ref import CommercialProfileEligibilityRef
from .commercial_profile_ref import CommercialProfileRef
from .common_section_ref import CommonSectionRef
from .companion_profile_ref import CompanionProfileRef
from .complex_feature_projection import ComplexFeatureProjection
from .complex_feature_projection_ref import ComplexFeatureProjectionRef
from .composite_frame_ref import CompositeFrameRef
from .compound_block_ref import CompoundBlockRef
from .compound_train_ref import CompoundTrainRef
from .connection_ref import ConnectionRef
from .contact_ref import ContactRef
from .control_centre_ref import ControlCentreRef
from .controllable_element_in_sequence_ref import ControllableElementInSequenceRef
from .controllable_element_price_ref import ControllableElementPriceRef
from .controllable_element_ref import ControllableElementRef
from .coupled_journey_ref import CoupledJourneyRef
from .course_of_journeys_ref import CourseOfJourneysRef
from .crew_base_ref import CrewBaseRef
from .customer_account_ref import CustomerAccountRef
from .customer_account_security_listing_ref import CustomerAccountSecurityListingRef
from .customer_account_status_ref import CustomerAccountStatusRef
from .customer_payment_means_ref import CustomerPaymentMeansRef
from .customer_purchase_package_element_ref import CustomerPurchasePackageElementRef
from .customer_purchase_package_price_ref import CustomerPurchasePackagePriceRef
from .customer_purchase_package_ref import CustomerPurchasePackageRef
from .customer_ref import CustomerRef
from .customer_security_listing_ref import CustomerSecurityListingRef
from .cycle_model_profile_ref import CycleModelProfileRef
from .data_source_ref import DataSourceRef
from .dated_special_service_ref import DatedSpecialServiceRef
from .dated_vehicle_journey_ref import DatedVehicleJourneyRef
from .day_type_ref import DayTypeRef
from .dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from .dead_run_ref import DeadRunRef
from .deck_entrance_couple_ref import DeckEntranceCoupleRef
from .deck_entrance_usage_ref import DeckEntranceUsageRef
from .deck_level_ref import DeckLevelRef
from .deck_navigation_path_ref import DeckNavigationPathRef
from .deck_path_junction_ref import DeckPathJunctionRef
from .deck_path_link_ref import DeckPathLinkRef
from .deck_plan_ref import DeckPlanRef
from .deck_ref import DeckRef
from .deck_space_capacity_ref import DeckSpaceCapacityRef
from .deck_vehicle_entrance_ref import DeckVehicleEntranceRef
from .deck_window_ref import DeckWindowRef
from .default_connection_ref import DefaultConnectionRef
from .default_dead_run_run_time_ref import DefaultDeadRunRunTimeRef
from .default_interchange_ref import DefaultInterchangeRef
from .default_service_journey_time_ref import DefaultServiceJourneyTimeRef
from .delivery_variant_ref import DeliveryVariantRef
from .department_ref import DepartmentRef
from .destination_display_ref import DestinationDisplayRef
from .destination_display_variant_ref import DestinationDisplayVariantRef
from .direction_ref import DirectionRef
from .discounting_rule_ref import DiscountingRuleRef
from .distance_matrix_element_inverse_ref import DistanceMatrixElementInverseRef
from .distance_matrix_element_price_ref import DistanceMatrixElementPriceRef
from .distance_matrix_element_ref import DistanceMatrixElementRef
from .distribution_channel_ref import DistributionChannelRef
from .driver_ref import DriverRef
from .driver_schedule_frame_ref import DriverScheduleFrameRef
from .driver_trip_ref import DriverTripRef
from .driver_trip_time_ref import DriverTripTimeRef
from .duty_part_ref import DutyPartRef
from .duty_ref import DutyRef
from .eligibility_change_policy_ref import EligibilityChangePolicyRef
from .emv_card_ref import EmvCardRef
from .entitlement_given_ref import EntitlementGivenRef
from .entitlement_product_ref import EntitlementProductRef
from .entitlement_required_ref import EntitlementRequiredRef
from .entity_in_version_structure import VersionedChildStructure
from .entrance_ref import EntranceRef
from .equipment_place_ref import EquipmentPlaceRef
from .equipment_position_ref import EquipmentPositionRef
from .estimated_passing_time_ref import EstimatedPassingTimeRef
from .exchanging_ref import ExchangingRef
from .facility_ref import FacilityRef
from .facility_requirement_ref import FacilityRequirementRef
from .facility_set_ref import FacilitySetRef
from .fare_contract_entry_ref import FareContractEntryRef
from .fare_contract_ref import FareContractRef
from .fare_contract_security_listing_ref import FareContractSecurityListingRef
from .fare_day_type_ref import FareDayTypeRef
from .fare_debit_ref import FareDebitRef
from .fare_demand_factor_ref import FareDemandFactorRef
from .fare_frame_ref import FareFrameRef
from .fare_price_ref import FarePriceRef
from .fare_product_price_ref import FareProductPriceRef
from .fare_product_ref import FareProductRef
from .fare_product_sale_debit_ref import FareProductSaleDebitRef
from .fare_quota_factor_ref import FareQuotaFactorRef
from .fare_request_ref import FareRequestRef
from .fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from .fare_section_ref import FareSectionRef
from .fare_structure_element_in_sequence_ref import FareStructureElementInSequenceRef
from .fare_structure_element_price_ref import FareStructureElementPriceRef
from .fare_structure_element_ref import FareStructureElementRef
from .fare_table_column_ref import FareTableColumnRef
from .fare_table_ref import FareTableRef
from .fare_table_row_ref import FareTableRowRef
from .fare_zone_ref import FareZoneRef
from .fleet_ref import FleetRef
from .flexible_area_ref import FlexibleAreaRef
from .flexible_line_ref import FlexibleLineRef
from .flexible_link_properties_ref import FlexibleLinkPropertiesRef
from .flexible_mode_of_operation_ref import FlexibleModeOfOperationRef
from .flexible_point_properties_ref import FlexiblePointPropertiesRef
from .flexible_quay_ref import FlexibleQuayRef
from .flexible_service_properties_ref import FlexibleServicePropertiesRef
from .flexible_stop_place_ref import FlexibleStopPlaceRef
from .frequency_of_use_ref import FrequencyOfUseRef
from .fulfilment_method_price_ref import FulfilmentMethodPriceRef
from .fulfilment_method_ref import FulfilmentMethodRef
from .garage_point_ref import GaragePointRef
from .garage_ref import GarageRef
from .general_frame_ref import GeneralFrameRef
from .general_group_of_entities_ref import GeneralGroupOfEntitiesRef
from .general_organisation_ref import GeneralOrganisationRef
from .general_section_ref import GeneralSectionRef
from .generic_navigation_path_ref import GenericNavigationPathRef
from .generic_path_junction_ref import GenericPathJunctionRef
from .generic_path_link_ref import GenericPathLinkRef
from .geographical_interval_price_ref import GeographicalIntervalPriceRef
from .geographical_interval_ref import GeographicalIntervalRef
from .geographical_structure_factor_ref import GeographicalStructureFactorRef
from .geographical_unit_price_ref import GeographicalUnitPriceRef
from .geographical_unit_ref import GeographicalUnitRef
from .group_of_customer_purchase_packages_ref import GroupOfCustomerPurchasePackagesRef
from .group_of_distance_matrix_elements_ref import GroupOfDistanceMatrixElementsRef
from .group_of_distribution_channels_ref import GroupOfDistributionChannelsRef
from .group_of_lines_ref import GroupOfLinesRef
from .group_of_operators_ref import GroupOfOperatorsRef
from .group_of_places_ref import GroupOfPlacesRef
from .group_of_sales_offer_packages_ref import GroupOfSalesOfferPackagesRef
from .group_of_services_ref import GroupOfServicesRef
from .group_of_single_journeys_ref import GroupOfSingleJourneysRef
from .group_of_sites_ref import GroupOfSitesRef
from .group_of_stop_places_ref import GroupOfStopPlacesRef
from .group_of_tariff_zones_ref import GroupOfTariffZonesRef
from .group_of_timebands_ref import GroupOfTimebandsRef
from .group_of_timing_links_ref import GroupOfTimingLinksRef
from .group_ticket_ref import GroupTicketRef
from .hail_and_ride_area_ref import HailAndRideAreaRef
from .headway_journey_group_ref import HeadwayJourneyGroupRef
from .individual_passenger_info_ref import IndividualPassengerInfoRef
from .individual_traveller_ref import IndividualTravellerRef
from .info_link import InfoLink
from .infrastructure_frame_ref import InfrastructureFrameRef
from .interchange_ref import InterchangeRef
from .interchange_rule_ref import InterchangeRuleRef
from .interchange_rule_timing_ref import InterchangeRuleTimingRef
from .interchanging_ref import InterchangingRef
from .journey_frequency_group_ref import JourneyFrequencyGroupRef
from .journey_meeting_ref import JourneyMeetingRef
from .journey_part_couple_ref import JourneyPartCoupleRef
from .journey_part_ref import JourneyPartRef
from .journey_pattern_headway_ref import JourneyPatternHeadwayRef
from .journey_pattern_layover_ref import JourneyPatternLayoverRef
from .journey_pattern_ref import JourneyPatternRef
from .journey_pattern_run_time_ref import JourneyPatternRunTimeRef
from .journey_pattern_wait_time_ref import JourneyPatternWaitTimeRef
from .journey_timing_ref import JourneyTimingRef
from .layer_ref import LayerRef
from .level_in_structure_ref import LevelInStructureRef
from .level_ref import LevelRef
from .limiting_rule_ref import LimitingRuleRef
from .line_link_ref import LineLinkRef
from .line_network_ref import LineNetworkRef
from .line_ref import LineRef
from .line_section_ref import LineSectionRef
from .link_projection import LinkProjection
from .link_projection_ref import LinkProjectionRef
from .link_sequence_projection import LinkSequenceProjection
from .link_sequence_projection_ref import LinkSequenceProjectionRef
from .link_sequence_ref import LinkSequenceRef
from .log_entry_ref import LogEntryRef
from .log_ref import LogRef
from .logical_display_ref import LogicalDisplayRef
from .luggage_allowance_ref import LuggageAllowanceRef
from .luggage_spot_ref import LuggageSpotRef
from .management_agent_ref import ManagementAgentRef
from .medium_access_device_security_listing_ref import MediumAccessDeviceSecurityListingRef
from .medium_application_instance_ref import MediumApplicationInstanceRef
from .minimum_stay_ref import MinimumStayRef
from .mobile_device_ref import MobileDeviceRef
from .mobility_journey_frame_ref import MobilityJourneyFrameRef
from .mobility_service_constraint_zone_ref import MobilityServiceConstraintZoneRef
from .mobility_service_frame_ref import MobilityServiceFrameRef
from .mode_ref import ModeRef
from .mode_restriction_assessment_ref import ModeRestrictionAssessmentRef
from .monitored_vehicle_sharing_parking_bay_ref import MonitoredVehicleSharingParkingBayRef
from .month_validity_offset_ref import MonthValidityOffsetRef
from .multilingual_string import MultilingualString
from .navigation_path_ref import NavigationPathRef
from .network_ref import NetworkRef
from .normal_dated_vehicle_journey_ref import NormalDatedVehicleJourneyRef
from .notice_ref import NoticeRef
from .observed_passing_time_ref import ObservedPassingTimeRef
from .off_site_path_link_ref import OffSitePathLinkRef
from .offence_debit_ref import OffenceDebitRef
from .offered_travel_specification_ref import OfferedTravelSpecificationRef
from .onboard_stay_ref import OnboardStayRef
from .online_service_operator_ref import OnlineServiceOperatorRef
from .onward_vehicle_meeting_link_ref import OnwardVehicleMeetingLinkRef
from .open_transport_mode_ref import OpenTransportModeRef
from .operating_day_ref import OperatingDayRef
from .operating_department_ref import OperatingDepartmentRef
from .operating_period_ref import OperatingPeriodRef
from .operational_context_ref import OperationalContextRef
from .operator_ref import OperatorRef
from .organisation_part_ref import OrganisationPartRef
from .organisation_ref import OrganisationRef
from .organisational_unit_ref import OrganisationalUnitRef
from .other_debit_ref import OtherDebitRef
from .other_deck_entrance_ref import OtherDeckEntranceRef
from .other_deck_space_ref import OtherDeckSpaceRef
from .other_organisation_ref import OtherOrganisationRef
from .parent_common_section_ref import ParentCommonSectionRef
from .parent_section_ref import ParentSectionRef
from .parking_area_ref import ParkingAreaRef
from .parking_bay_condition_ref import ParkingBayConditionRef
from .parking_bay_ref import ParkingBayRef
from .parking_bay_status_ref import ParkingBayStatusRef
from .parking_capacity_ref import ParkingCapacityRef
from .parking_charge_band_ref import ParkingChargeBandRef
from .parking_entrance_for_vehicles_ref import ParkingEntranceForVehiclesRef
from .parking_entrance_ref import ParkingEntranceRef
from .parking_passenger_entrance_ref import ParkingPassengerEntranceRef
from .parking_point_ref import ParkingPointRef
from .parking_price_ref import ParkingPriceRef
from .parking_properties_ref import ParkingPropertiesRef
from .parking_ref import ParkingRef
from .parking_tariff_ref import ParkingTariffRef
from .passenger_at_stop_time_ref import PassengerAtStopTimeRef
from .passenger_capacity_ref import PassengerCapacityRef
from .passenger_carrying_requirement_ref import PassengerCarryingRequirementRef
from .passenger_entrance_ref import PassengerEntranceRef
from .passenger_seat_ref import PassengerSeatRef
from .passenger_space_ref import PassengerSpaceRef
from .passenger_spot_ref import PassengerSpotRef
from .passenger_vehicle_capacity_ref import PassengerVehicleCapacityRef
from .passenger_vehicle_spot_ref import PassengerVehicleSpotRef
from .path_instruction_ref import PathInstructionRef
from .path_junction_ref import PathJunctionRef
from .path_link_ref import PathLinkRef
from .penalty_policy_ref import PenaltyPolicyRef
from .personal_mode_of_operation_ref import PersonalModeOfOperationRef
from .place_ref import PlaceRef
from .point_of_interest_classification_ref import PointOfInterestClassificationRef
from .point_of_interest_entrance_ref import PointOfInterestEntranceRef
from .point_of_interest_hierarchy_ref import PointOfInterestHierarchyRef
from .point_of_interest_ref import PointOfInterestRef
from .point_of_interest_space_ref import PointOfInterestSpaceRef
from .point_of_interest_vehicle_entrance_ref import PointOfInterestVehicleEntranceRef
from .point_projection import PointProjection
from .point_projection_ref import PointProjectionRef
from .point_ref import PointRef
from .pool_of_vehicles_ref import PoolOfVehiclesRef
from .postal_address_ref import PostalAddressRef
from .powered_train_ref import PoweredTrainRef
from .preassigned_fare_product_ref import PreassignedFareProductRef
from .price_group_ref import PriceGroupRef
from .price_unit_ref import PriceUnitRef
from .priceable_object_ref import PriceableObjectRef
from .pricing_parameter_set_ref import PricingParameterSetRef
from .pricing_rule_ref import PricingRuleRef
from .pricing_service_ref import PricingServiceRef
from .profile_parameter_ref import ProfileParameterRef
from .purchase_window_ref import PurchaseWindowRef
from .purpose_of_equipment_profile_ref import PurposeOfEquipmentProfileRef
from .purpose_of_grouping_ref import PurposeOfGroupingRef
from .purpose_of_journey_partition_ref import PurposeOfJourneyPartitionRef
from .quality_structure_factor_price_ref import QualityStructureFactorPriceRef
from .quality_structure_factor_ref import QualityStructureFactorRef
from .quay_ref import QuayRef
from .railway_link_ref import RailwayLinkRef
from .railway_point_ref import RailwayPointRef
from .recharging_equipment_profile_ref import RechargingEquipmentProfileRef
from .recharging_plan_ref import RechargingPlanRef
from .recharging_step_ref import RechargingStepRef
from .refunding_ref import RefundingRef
from .relief_opportunity_ref import ReliefOpportunityRef
from .relief_point_ref import ReliefPointRef
from .rental_availability_ref import RentalAvailabilityRef
from .rental_option_ref import RentalOptionRef
from .rental_penalty_policy_ref import RentalPenaltyPolicyRef
from .repeated_trip_fare_request_ref import RepeatedTripFareRequestRef
from .replacing_ref import ReplacingRef
from .requested_travel_specification_ref import RequestedTravelSpecificationRef
from .reselling_ref import ResellingRef
from .reserving_ref import ReservingRef
from .residential_qualification_eligibility_ref import ResidentialQualificationEligibilityRef
from .residential_qualification_ref import ResidentialQualificationRef
from .resource_frame_ref import ResourceFrameRef
from .responsibility_role_ref import ResponsibilityRoleRef
from .responsibility_set_ref import ResponsibilitySetRef
from .restricted_service_facility_set_ref import RestrictedServiceFacilitySetRef
from .retail_consortium_ref import RetailConsortiumRef
from .retail_device_security_listing_ref import RetailDeviceSecurityListingRef
from .rhythmical_journey_group_ref import RhythmicalJourneyGroupRef
from .road_address_ref import RoadAddressRef
from .road_link_ref import RoadLinkRef
from .road_point_ref import RoadPointRef
from .rolling_stock_inventory_ref import RollingStockInventoryRef
from .round_trip_ref import RoundTripRef
from .rounding_ref import RoundingRef
from .rounding_step_ref import RoundingStepRef
from .route_instruction_ref import RouteInstructionRef
from .route_link_ref import RouteLinkRef
from .route_point_ref import RoutePointRef
from .route_ref import RouteRef
from .routing_constraint_zone_ref import RoutingConstraintZoneRef
from .routing_ref import RoutingRef
from .sale_discount_right_ref import SaleDiscountRightRef
from .sales_offer_package_element_ref import SalesOfferPackageElementRef
from .sales_offer_package_entitlement_given_ref import SalesOfferPackageEntitlementGivenRef
from .sales_offer_package_entitlement_required_ref import SalesOfferPackageEntitlementRequiredRef
from .sales_offer_package_price_ref import SalesOfferPackagePriceRef
from .sales_offer_package_ref import SalesOfferPackageRef
from .sales_transaction_frame_ref import SalesTransactionFrameRef
from .sales_transaction_ref import SalesTransactionRef
from .schedule_request_ref import ScheduleRequestRef
from .scheduled_mode_of_operation_ref import ScheduledModeOfOperationRef
from .scheduled_stop_point_ref import ScheduledStopPointRef
from .schematic_map_member_ref import SchematicMapMemberRef
from .schematic_map_ref import SchematicMapRef
from .section_ref import SectionRef
from .sensor_in_entrance_ref import SensorInEntranceRef
from .sensor_in_spot_ref import SensorInSpotRef
from .series_constraint_price_ref import SeriesConstraintPriceRef
from .series_constraint_ref import SeriesConstraintRef
from .service_access_code_ref import ServiceAccessCodeRef
from .service_access_right_ref import ServiceAccessRightRef
from .service_calendar_frame_ref import ServiceCalendarFrameRef
from .service_calendar_ref import ServiceCalendarRef
from .service_facility_set_ref import ServiceFacilitySetRef
from .service_frame_ref import ServiceFrameRef
from .service_journey_interchange_ref import ServiceJourneyInterchangeRef
from .service_journey_pattern_interchange_ref import ServiceJourneyPatternInterchangeRef
from .service_journey_pattern_ref import ServiceJourneyPatternRef
from .service_journey_ref import ServiceJourneyRef
from .service_link_ref import ServiceLinkRef
from .service_pattern_ref import ServicePatternRef
from .service_site_ref import ServiceSiteRef
from .serviced_organisation_ref import ServicedOrganisationRef
from .simple_vehicle_type_ref import SimpleVehicleTypeRef
from .single_journey_path_ref import SingleJourneyPathRef
from .single_journey_ref import SingleJourneyRef
from .single_trip_fare_request_ref import SingleTripFareRequestRef
from .site_component_ref import SiteComponentRef
from .site_connection_ref import SiteConnectionRef
from .site_element_ref import SiteElementRef
from .site_facility_set_ref import SiteFacilitySetRef
from .site_frame_ref import SiteFrameRef
from .site_navigation_path_ref import SiteNavigationPathRef
from .site_path_junction_ref import SitePathJunctionRef
from .site_path_link_ref import SitePathLinkRef
from .site_ref import SiteRef
from .site_structure_ref import SiteStructureRef
from .smartcard_ref import SmartcardRef
from .special_service_ref import SpecialServiceRef
from .spot_affinity_ref import SpotAffinityRef
from .spot_column_ref import SpotColumnRef
from .spot_row_ref import SpotRowRef
from .standard_fare_table_ref import StandardFareTableRef
from .start_time_at_stop_point_ref import StartTimeAtStopPointRef
from .step_limit_ref import StepLimitRef
from .stop_area_ref import StopAreaRef
from .stop_event_request_ref import StopEventRequestRef
from .stop_finder_request_ref import StopFinderRequestRef
from .stop_place_entrance_ref import StopPlaceEntranceRef
from .stop_place_ref import StopPlaceRef
from .stop_place_space_ref import StopPlaceSpaceRef
from .stop_place_vehicle_entrance_ref import StopPlaceVehicleEntranceRef
from .submode_ref import SubmodeRef
from .subscribing_ref import SubscribingRef
from .supplement_product_ref import SupplementProductRef
from .suspending_ref import SuspendingRef
from .target_passing_time_ref import TargetPassingTimeRef
from .tariff_object_ref import TariffObjectRef
from .tariff_ref import TariffRef
from .tariff_zone_ref import TariffZoneRef
from .taxi_parking_area_ref import TaxiParkingAreaRef
from .taxi_rank_ref import TaxiRankRef
from .taxi_stand_ref import TaxiStandRef
from .template_service_journey_ref import TemplateServiceJourneyRef
from .third_party_product_ref import ThirdPartyProductRef
from .time_demand_profile_ref import TimeDemandProfileRef
from .time_demand_type_ref import TimeDemandTypeRef
from .time_interval_price_ref import TimeIntervalPriceRef
from .time_interval_ref import TimeIntervalRef
from .time_structure_factor_ref import TimeStructureFactorRef
from .time_unit_price_ref import TimeUnitPriceRef
from .time_unit_ref import TimeUnitRef
from .timeband_ref import TimebandRef
from .timetable_frame_ref import TimetableFrameRef
from .timetabled_passing_time_ref import TimetabledPassingTimeRef
from .timing_algorithm_type_ref import TimingAlgorithmTypeRef
from .timing_link_ref import TimingLinkRef
from .timing_pattern_ref import TimingPatternRef
from .timing_point_ref import TimingPointRef
from .topographic_place_ref import TopographicPlaceRef
from .topographic_projection import TopographicProjection
from .topographic_projection_ref import TopographicProjectionRef
from .tractive_element_type_ref import TractiveElementTypeRef
from .tractive_rolling_stock_item_ref import TractiveRollingStockItemRef
from .traffic_control_point_ref import TrafficControlPointRef
from .trailing_element_type_ref import TrailingElementTypeRef
from .trailing_rolling_stock_item_ref import TrailingRollingStockItemRef
from .train_block_part_ref import TrainBlockPartRef
from .train_block_ref import TrainBlockRef
from .train_component_ref import TrainComponentRef
from .train_element_ref import TrainElementRef
from .train_element_type_ref import TrainElementTypeRef
from .train_in_compound_train_ref import TrainInCompoundTrainRef
from .train_number_ref import TrainNumberRef
from .train_ref import TrainRef
from .transferability_ref import TransferabilityRef
from .transport_administrative_zone_ref import TransportAdministrativeZoneRef
from .transport_type_ref import TransportTypeRef
from .travel_agent_ref import TravelAgentRef
from .travel_document_ref import TravelDocumentRef
from .travel_document_security_listing_ref import TravelDocumentSecurityListingRef
from .travel_specification_ref import TravelSpecificationRef
from .trip_debit_ref import TripDebitRef
from .trip_leg_ref import TripLegRef
from .trip_pattern_trip_ref import TripPatternTripRef
from .trip_plan_request_ref import TripPlanRequestRef
from .trip_ref import TripRef
from .turnaround_time_limit_time_ref import TurnaroundTimeLimitTimeRef
from .type_of_access_right_assignment_ref import TypeOfAccessRightAssignmentRef
from .type_of_activation_ref import TypeOfActivationRef
from .type_of_battery_chemistry_ref import TypeOfBatteryChemistryRef
from .type_of_codespace_assignment_ref import TypeOfCodespaceAssignmentRef
from .type_of_concession_ref import TypeOfConcessionRef
from .type_of_congestion_ref import TypeOfCongestionRef
from .type_of_customer_account_ref import TypeOfCustomerAccountRef
from .type_of_deck_entrance_ref import TypeOfDeckEntranceRef
from .type_of_deck_space_ref import TypeOfDeckSpaceRef
from .type_of_delivery_variant_ref import TypeOfDeliveryVariantRef
from .type_of_driver_permit_ref import TypeOfDriverPermitRef
from .type_of_equipment_ref import TypeOfEquipmentRef
from .type_of_facility_ref import TypeOfFacilityRef
from .type_of_fare_contract_entry_ref import TypeOfFareContractEntryRef
from .type_of_fare_contract_ref import TypeOfFareContractRef
from .type_of_fare_product_ref import TypeOfFareProductRef
from .type_of_fare_structure_element_ref import TypeOfFareStructureElementRef
from .type_of_fare_structure_factor_ref import TypeOfFareStructureFactorRef
from .type_of_fare_table_ref import TypeOfFareTableRef
from .type_of_feature_ref import TypeOfFeatureRef
from .type_of_fleet_ref import TypeOfFleetRef
from .type_of_flexible_service_ref import TypeOfFlexibleServiceRef
from .type_of_frame_ref import TypeOfFrameRef
from .type_of_journey_pattern_ref import TypeOfJourneyPatternRef
from .type_of_line_ref import TypeOfLineRef
from .type_of_link_ref import TypeOfLinkRef
from .type_of_link_sequence_ref import TypeOfLinkSequenceRef
from .type_of_locatable_spot_ref import TypeOfLocatableSpotRef
from .type_of_machine_readability_ref import TypeOfMachineReadabilityRef
from .type_of_medium_access_device_ref import TypeOfMediumAccessDeviceRef
from .type_of_mobility_service_ref import TypeOfMobilityServiceRef
from .type_of_mode_of_operation_ref import TypeOfModeOfOperationRef
from .type_of_notice_ref import TypeOfNoticeRef
from .type_of_operation_ref import TypeOfOperationRef
from .type_of_organisation_part_ref import TypeOfOrganisationPartRef
from .type_of_organisation_ref import TypeOfOrganisationRef
from .type_of_parking_ref import TypeOfParkingRef
from .type_of_passenger_information_equipment_ref import TypeOfPassengerInformationEquipmentRef
from .type_of_payment_method_ref import TypeOfPaymentMethodRef
from .type_of_place_ref import TypeOfPlaceRef
from .type_of_plug_ref import TypeOfPlugRef
from .type_of_point_ref import TypeOfPointRef
from .type_of_pricing_rule_ref import TypeOfPricingRuleRef
from .type_of_product_category_ref import TypeOfProductCategoryRef
from .type_of_projection_ref import TypeOfProjectionRef
from .type_of_proof_ref import TypeOfProofRef
from .type_of_responsibility_role_ref import TypeOfResponsibilityRoleRef
from .type_of_retail_device_ref import TypeOfRetailDeviceRef
from .type_of_rolling_stock_ref import TypeOfRollingStockRef
from .type_of_sales_offer_package_ref import TypeOfSalesOfferPackageRef
from .type_of_security_list_ref import TypeOfSecurityListRef
from .type_of_service_feature_ref import TypeOfServiceFeatureRef
from .type_of_service_ref import TypeOfServiceRef
from .type_of_tariff_ref import TypeOfTariffRef
from .type_of_time_demand_type_ref import TypeOfTimeDemandTypeRef
from .type_of_transfer_ref import TypeOfTransferRef
from .type_of_travel_document_ref import TypeOfTravelDocumentRef
from .type_of_usage_parameter_ref import TypeOfUsageParameterRef
from .type_of_validity_ref import TypeOfValidityRef
from .type_of_zone_ref import TypeOfZoneRef
from .uic_operating_period_ref import UicOperatingPeriodRef
from .unpowered_train_ref import UnpoweredTrainRef
from .usage_discount_right_ref import UsageDiscountRightRef
from .usage_parameter_price_ref import UsageParameterPriceRef
from .usage_validity_period_ref import UsageValidityPeriodRef
from .user_profile_eligibility_ref import UserProfileEligibilityRef
from .user_profile_ref import UserProfileRef
from .validable_element_price_ref import ValidableElementPriceRef
from .validable_element_ref import ValidableElementRef
from .validity_condition_ref import ValidityConditionRef
from .validity_rule_parameter_ref import ValidityRuleParameterRef
from .validity_trigger_ref import ValidityTriggerRef
from .vehicle_entrance_ref import VehicleEntranceRef
from .vehicle_equipment_profile_member_ref import VehicleEquipmentProfileMemberRef
from .vehicle_equipment_profile_ref import VehicleEquipmentProfileRef
from .vehicle_journey_ref import VehicleJourneyRef
from .vehicle_manoeuvring_requirement_ref import VehicleManoeuvringRequirementRef
from .vehicle_meeting_link_ref import VehicleMeetingLinkRef
from .vehicle_meeting_place_ref import VehicleMeetingPlaceRef
from .vehicle_meeting_point_ref import VehicleMeetingPointRef
from .vehicle_model_ref import VehicleModelRef
from .vehicle_pooler_profile_ref import VehiclePoolerProfileRef
from .vehicle_pooling_driver_info_ref import VehiclePoolingDriverInfoRef
from .vehicle_pooling_meeting_place_ref import VehiclePoolingMeetingPlaceRef
from .vehicle_pooling_parking_area_ref import VehiclePoolingParkingAreaRef
from .vehicle_pooling_parking_bay_ref import VehiclePoolingParkingBayRef
from .vehicle_pooling_ref import VehiclePoolingRef
from .vehicle_position_alignment_ref import VehiclePositionAlignmentRef
from .vehicle_profile_ref import VehicleProfileRef
from .vehicle_quay_alignment_ref import VehicleQuayAlignmentRef
from .vehicle_ref import VehicleRef
from .vehicle_rental_ref import VehicleRentalRef
from .vehicle_requirement_ref import VehicleRequirementRef
from .vehicle_schedule_frame_ref import VehicleScheduleFrameRef
from .vehicle_service_part_ref import VehicleServicePartRef
from .vehicle_service_ref import VehicleServiceRef
from .vehicle_sharing_parking_area_ref import VehicleSharingParkingAreaRef
from .vehicle_sharing_parking_bay_ref import VehicleSharingParkingBayRef
from .vehicle_sharing_ref import VehicleSharingRef
from .vehicle_stopping_place_ref import VehicleStoppingPlaceRef
from .vehicle_stopping_position_ref import VehicleStoppingPositionRef
from .vehicle_type_preference_ref import VehicleTypePreferenceRef
from .vehicle_type_ref import VehicleTypeRef
from .vehicle_type_zone_restriction_ref import VehicleTypeZoneRestrictionRef
from .version_of_object_ref import VersionOfObjectRef
from .version_ref import VersionRef
from .whitelist_ref import WhitelistRef
from .wire_link_ref import WireLinkRef
from .wire_point_ref import WirePointRef
from .zone_in_series_ref import ZoneInSeriesRef
from .zone_projection import ZoneProjection
from .zone_projection_ref import ZoneProjectionRef
from .zone_ref import ZoneRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SchematicMapMemberVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "SchematicMapMember_VersionedChildStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice: Optional[
        Union[
            TripLegRef,
            IndividualPassengerInfoRef,
            VehiclePoolingDriverInfoRef,
            IndividualTravellerRef,
            ServiceAccessCodeRef,
            TravelDocumentRef,
            RepeatedTripFareRequestRef,
            SingleTripFareRequestRef,
            FareRequestRef,
            StopFinderRequestRef,
            StopEventRequestRef,
            ScheduleRequestRef,
            TripPlanRequestRef,
            CustomerPaymentMeansRef,
            ResidentialQualificationEligibilityRef,
            CommercialProfileEligibilityRef,
            UserProfileEligibilityRef,
            CustomerAccountRef,
            FareContractRef,
            CustomerRef,
            VehicleTypeZoneRestrictionRef,
            MediumApplicationInstanceRef,
            MobileDeviceRef,
            EmvCardRef,
            SmartcardRef,
            StartTimeAtStopPointRef,
            ResidentialQualificationRef,
            TypeOfConcessionRef,
            TypeOfUsageParameterRef,
            ZoneInSeriesRef,
            TariffObjectRef,
            ParkingTariffRef,
            TariffRef,
            TypeOfFareTableRef,
            FareTableRowRef,
            FareTableColumnRef,
            TimeUnitRef,
            GeographicalUnitRef,
            ControllableElementInSequenceRef,
            FareStructureElementInSequenceRef,
            AccessRightInProductRef,
            CellRef,
            CustomerPurchasePackagePriceRef,
            ParkingPriceRef,
            TimeIntervalPriceRef,
            TimeUnitPriceRef,
            QualityStructureFactorPriceRef,
            ControllableElementPriceRef,
            ValidableElementPriceRef,
            GeographicalIntervalPriceRef,
            GeographicalUnitPriceRef,
            UsageParameterPriceRef,
            SeriesConstraintPriceRef,
            SalesOfferPackagePriceRef,
            DistanceMatrixElementPriceRef,
            FareStructureElementPriceRef,
            FulfilmentMethodPriceRef,
            CappingRulePriceRef,
            FareProductPriceRef,
            FarePriceRef,
            CustomerPurchasePackageElementRef,
            CustomerPurchasePackageRef,
            ControllableElementRef,
            ValidableElementRef,
            AdditionalDriverOptionRef,
            RentalOptionRef,
            RentalPenaltyPolicyRef,
            SalesOfferPackageEntitlementGivenRef,
            SalesOfferPackageEntitlementRequiredRef,
            MinimumStayRef,
            InterchangingRef,
            FrequencyOfUseRef,
            SuspendingRef,
            UsageValidityPeriodRef,
            StepLimitRef,
            RoutingRef,
            RoundTripRef,
            LuggageAllowanceRef,
            EntitlementGivenRef,
            EntitlementRequiredRef,
            EligibilityChangePolicyRef,
            GroupTicketRef,
            CommercialProfileRef,
            VehiclePoolerProfileRef,
            CompanionProfileRef,
            UserProfileRef,
            ProfileParameterRef,
            SubscribingRef,
            PenaltyPolicyRef,
            ChargingPolicyRef,
            TransferabilityRef,
            ReplacingRef,
            RefundingRef,
            ExchangingRef,
            ResellingRef,
            CancellingRef,
            ReservingRef,
            BookingPolicyRef,
            PurchaseWindowRef,
            SeriesConstraintRef,
            SalesOfferPackageElementRef,
            SalesOfferPackageRef,
            DistanceMatrixElementInverseRef,
            DistanceMatrixElementRef,
            FareStructureElementRef,
            FulfilmentMethodRef,
            CappingRuleRef,
            EntitlementProductRef,
            SupplementProductRef,
            PreassignedFareProductRef,
            AmountOfPriceUnitProductRef,
            UsageDiscountRightRef,
            ThirdPartyProductRef,
            CappedDiscountRightRef,
            SaleDiscountRightRef,
            FareProductRef,
            ServiceAccessRightRef,
            TimeIntervalRef,
            GeographicalIntervalRef,
            ParkingChargeBandRef,
            TimeStructureFactorRef,
            FareQuotaFactorRef,
            FareDemandFactorRef,
            QualityStructureFactorRef,
            GeographicalStructureFactorRef,
            PriceableObjectRef,
            MonthValidityOffsetRef,
            LimitingRuleRef,
            DiscountingRuleRef,
            PricingRuleRef,
            PricingServiceRef,
            RoundingStepRef,
            RoundingRef,
            PricingParameterSetRef,
            RechargingStepRef,
            RechargingPlanRef,
            FlexibleServicePropertiesRef,
            DriverTripTimeRef,
            DriverTripRef,
            DutyPartRef,
            AccountableElementRef,
            DutyRef,
            ReliefOpportunityRef,
            CourseOfJourneysRef,
            DriverRef,
            VehicleServicePartRef,
            VehicleServiceRef,
            CompoundBlockRef,
            TrainBlockPartRef,
            BlockPartRef,
            TrainBlockRef,
            BlockRef,
            JourneyPartCoupleRef,
            CoupledJourneyRef,
            JourneyPartRef,
            InterchangeRuleTimingRef,
            InterchangeRuleRef,
            ServiceJourneyPatternInterchangeRef,
            ServiceJourneyInterchangeRef,
            DefaultInterchangeRef,
            InterchangeRef,
            JourneyMeetingRef,
            PassengerAtStopTimeRef,
            TimetabledPassingTimeRef,
            EstimatedPassingTimeRef,
            ObservedPassingTimeRef,
            TargetPassingTimeRef,
            TrainNumberRef,
            RoutingConstraintZoneRef,
            VehiclePositionAlignmentRef,
            VehicleQuayAlignmentRef,
            LogicalDisplayRef,
            ParkingPropertiesRef,
            ParkingCapacityRef,
            LineNetworkRef,
            RouteInstructionRef,
            FlexiblePointPropertiesRef,
            FlexibleLinkPropertiesRef,
            TimeDemandProfileRef,
            TimeDemandTypeRef,
            VehicleTypePreferenceRef,
            JourneyPatternHeadwayRef,
            JourneyPatternLayoverRef,
            JourneyPatternRunTimeRef,
            JourneyPatternWaitTimeRef,
            DefaultServiceJourneyTimeRef,
            DefaultDeadRunRunTimeRef,
            TurnaroundTimeLimitTimeRef,
            JourneyTimingRef,
            CrewBaseRef,
            RollingStockInventoryRef,
            TrailingRollingStockItemRef,
            TractiveRollingStockItemRef,
            VehicleRef,
            SpotAffinityRef,
            TrainComponentRef,
            TrainElementRef,
            TrailingElementTypeRef,
            TractiveElementTypeRef,
            TrainElementTypeRef,
            TrainInCompoundTrainRef,
            PassengerSeatRef,
            TravelDocumentSecurityListingRef,
            RetailDeviceSecurityListingRef,
            CustomerAccountSecurityListingRef,
            FareContractSecurityListingRef,
            CustomerSecurityListingRef,
            MediumAccessDeviceSecurityListingRef,
            WhitelistRef,
            BlacklistRef,
            SchematicMapMemberRef,
            SchematicMapRef,
            CycleModelProfileRef,
            CarModelProfileRef,
            DeckSpaceCapacityRef,
            DeckLevelRef,
            DeckEntranceCoupleRef,
            DeckEntranceUsageRef,
            DeckRef,
            DeckPlanRef,
            DeckWindowRef,
            OtherDeckEntranceRef,
            DeckVehicleEntranceRef,
            PassengerEntranceRef,
            OtherDeckSpaceRef,
            PassengerSpaceRef,
            LuggageSpotRef,
            PassengerVehicleSpotRef,
            PassengerSpotRef,
            SpotColumnRef,
            SpotRowRef,
            SensorInEntranceRef,
            SensorInSpotRef,
            ModeRestrictionAssessmentRef,
            DeliveryVariantRef,
            NoticeRef,
            VehicleEquipmentProfileMemberRef,
            VehicleProfileRef,
            RechargingEquipmentProfileRef,
            VehicleEquipmentProfileRef,
            VehicleModelRef,
            PassengerVehicleCapacityRef,
            PassengerCapacityRef,
            FacilityRequirementRef,
            VehicleManoeuvringRequirementRef,
            PassengerCarryingRequirementRef,
            VehicleRequirementRef,
            SimpleVehicleTypeRef,
            CompoundTrainRef,
            UnpoweredTrainRef,
            PoweredTrainRef,
            TrainRef,
            VehicleTypeRef,
            TransportTypeRef,
            OnboardStayRef,
            AccommodationRef,
            RestrictedServiceFacilitySetRef,
            ServiceFacilitySetRef,
            SiteFacilitySetRef,
            FacilitySetRef,
            FacilityRef,
            OperatingDepartmentRef,
            OperationalContextRef,
            LevelInStructureRef,
            SiteStructureRef,
            LevelRef,
            ModeRef,
            SubmodeRef,
            OpenTransportModeRef,
            PathInstructionRef,
            OffenceDebitRef,
            FareProductSaleDebitRef,
            TripDebitRef,
            BookingDebitRef,
            OtherDebitRef,
            FareDebitRef,
            SalesTransactionRef,
            OfferedTravelSpecificationRef,
            RequestedTravelSpecificationRef,
            TravelSpecificationRef,
            FareContractEntryRef,
            LogEntryRef,
            TimebandRef,
            FareDayTypeRef,
            DayTypeRef,
            DefaultConnectionRef,
            SiteConnectionRef,
            ConnectionRef,
            AccessRef,
            HailAndRideAreaRef,
            FlexibleAreaRef,
            FlexibleQuayRef,
            FlexibleStopPlaceRef,
            EquipmentPlaceRef,
            EquipmentPositionRef,
            TopographicPlaceRef,
            VehiclePoolingMeetingPlaceRef,
            VehicleMeetingPlaceRef,
            GarageRef,
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
            AddressablePlaceRef,
            PostalAddressRef,
            RoadAddressRef,
            AddressRef,
            DeckPathJunctionRef,
            PathJunctionRef,
            SitePathJunctionRef,
            GenericPathJunctionRef,
            UicOperatingPeriodRef,
            OperatingPeriodRef,
            OperatingDayRef,
            ServiceCalendarRef,
            ContactRef,
            TopographicProjectionRef,
            ComplexFeatureProjectionRef,
            LinkSequenceProjectionRef,
            ZoneProjectionRef,
            LinkProjectionRef,
            PointProjectionRef,
            TripRef,
            TripPatternTripRef,
            SingleJourneyPathRef,
            SingleJourneyRef,
            NormalDatedVehicleJourneyRef,
            DatedVehicleJourneyRef,
            DatedSpecialServiceRef,
            SpecialServiceRef,
            TemplateServiceJourneyRef,
            ServiceJourneyRef,
            DeadRunRef,
            VehicleJourneyRef,
            ServiceJourneyPatternRef,
            ServicePatternRef,
            DeadRunJourneyPatternRef,
            JourneyPatternRef,
            TimingPatternRef,
            RouteRef,
            DeckNavigationPathRef,
            NavigationPathRef,
            SiteNavigationPathRef,
            GenericNavigationPathRef,
            LinkSequenceRef,
            OnwardVehicleMeetingLinkRef,
            VehicleMeetingLinkRef,
            ServiceLinkRef,
            LineLinkRef,
            TimingLinkRef,
            WireLinkRef,
            RoadLinkRef,
            RailwayLinkRef,
            ActivationLinkRef,
            RouteLinkRef,
            DeckPathLinkRef,
            OffSitePathLinkRef,
            PathLinkRef,
            SitePathLinkRef,
            GenericPathLinkRef,
            VehicleMeetingPointRef,
            WirePointRef,
            RoadPointRef,
            RailwayPointRef,
            TrafficControlPointRef,
            BeaconPointRef,
            ActivationPointRef,
            BorderPointRef,
            FareScheduledStopPointRef,
            ScheduledStopPointRef,
            GaragePointRef,
            ParkingPointRef,
            ReliefPointRef,
            TimingPointRef,
            RoutePointRef,
            PointRef,
            ResponsibilityRoleRef,
            AlternativeNameRef,
            AlternativeTextRef,
            AvailabilityConditionRef,
            ValidityRuleParameterRef,
            ValidityTriggerRef,
            ValidityConditionRef,
            ControlCentreRef,
            OrganisationalUnitRef,
            DepartmentRef,
            OrganisationPartRef,
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
            ResponsibilitySetRef,
            DestinationDisplayVariantRef,
            DestinationDisplayRef,
            AllowedLineDirectionRef,
            FlexibleLineRef,
            LineRef,
            GroupOfCustomerPurchasePackagesRef,
            PoolOfVehiclesRef,
            GroupOfSalesOfferPackagesRef,
            GroupOfDistanceMatrixElementsRef,
            GroupOfDistributionChannelsRef,
            GroupOfSingleJourneysRef,
            StandardFareTableRef,
            FareTableRef,
            PriceGroupRef,
            RhythmicalJourneyGroupRef,
            HeadwayJourneyGroupRef,
            JourneyFrequencyGroupRef,
            GroupOfServicesRef,
            PointOfInterestHierarchyRef,
            GroupOfTimingLinksRef,
            FleetRef,
            GroupOfStopPlacesRef,
            GroupOfOperatorsRef,
            GroupOfSitesRef,
            GroupOfPlacesRef,
            ParentSectionRef,
            ParentCommonSectionRef,
            CommonSectionRef,
            LineSectionRef,
            FareSectionRef,
            GeneralSectionRef,
            SectionRef,
            LogRef,
            GroupOfTimebandsRef,
            PlaceRef,
            GroupOfTariffZonesRef,
            MobilityServiceConstraintZoneRef,
            StopAreaRef,
            TransportAdministrativeZoneRef,
            AccessZoneRef,
            AdministrativeZoneRef,
            FareZoneRef,
            TariffZoneRef,
            ZoneRef,
            LayerRef,
            NetworkRef,
            GroupOfLinesRef,
            GeneralGroupOfEntitiesRef,
            MobilityJourneyFrameRef,
            MobilityServiceFrameRef,
            SalesTransactionFrameRef,
            FareFrameRef,
            ServiceFrameRef,
            DriverScheduleFrameRef,
            VehicleScheduleFrameRef,
            TimetableFrameRef,
            SiteFrameRef,
            InfrastructureFrameRef,
            GeneralFrameRef,
            ResourceFrameRef,
            ServiceCalendarFrameRef,
            CompositeFrameRef,
            ParkingBayConditionRef,
            RentalAvailabilityRef,
            ParkingBayStatusRef,
            TypeOfMediumAccessDeviceRef,
            TypeOfProofRef,
            DistributionChannelRef,
            ChargingMomentRef,
            PriceUnitRef,
            PurposeOfJourneyPartitionRef,
            TimingAlgorithmTypeRef,
            TypeOfParkingRef,
            PointOfInterestClassificationRef,
            TypeOfActivationRef,
            TypeOfFleetRef,
            TypeOfDeckEntranceRef,
            TypeOfDeckSpaceRef,
            TypeOfLocatableSpotRef,
            DirectionRef,
            TypeOfDriverPermitRef,
            AcceptedDriverPermitRef,
            PurposeOfEquipmentProfileRef,
            TypeOfProductCategoryRef,
            TypeOfPaymentMethodRef,
            ClassOfUseRef,
            TypeOfOperationRef,
            TypeOfCodespaceAssignmentRef,
            BrandingRef,
            TypeOfResponsibilityRoleRef,
            PurposeOfGroupingRef,
            TypeOfRetailDeviceRef,
            CustomerAccountStatusRef,
            TypeOfCustomerAccountRef,
            TypeOfFareContractEntryRef,
            TypeOfFareContractRef,
            TypeOfAccessRightAssignmentRef,
            TypeOfSalesOfferPackageRef,
            TypeOfFareStructureElementRef,
            TypeOfTariffRef,
            AllDistributionChannelsRef,
            TypeOfMachineReadabilityRef,
            TypeOfTravelDocumentRef,
            TypeOfMobilityServiceRef,
            TypeOfFareProductRef,
            TypeOfFareStructureFactorRef,
            TypeOfPricingRuleRef,
            TypeOfFlexibleServiceRef,
            TypeOfPassengerInformationEquipmentRef,
            TypeOfTimeDemandTypeRef,
            TypeOfJourneyPatternRef,
            TypeOfRollingStockRef,
            TypeOfSecurityListRef,
            TypeOfPlugRef,
            TypeOfBatteryChemistryRef,
            TypeOfServiceFeatureRef,
            TypeOfDeliveryVariantRef,
            TypeOfNoticeRef,
            TypeOfCongestionRef,
            TypeOfServiceRef,
            TypeOfFacilityRef,
            TypeOfModeOfOperationRef,
            PersonalModeOfOperationRef,
            VehiclePoolingRef,
            VehicleSharingRef,
            VehicleRentalRef,
            FlexibleModeOfOperationRef,
            ScheduledModeOfOperationRef,
            TypeOfEquipmentRef,
            TypeOfPlaceRef,
            TypeOfTransferRef,
            TypeOfOrganisationPartRef,
            TypeOfOrganisationRef,
            TypeOfZoneRef,
            TypeOfProjectionRef,
            TypeOfFeatureRef,
            TypeOfLinkSequenceRef,
            TypeOfLinkRef,
            TypeOfPointRef,
            TypeOfLineRef,
            TypeOfValidityRef,
            TypeOfFrameRef,
            DataSourceRef,
            VersionRef,
            VersionOfObjectRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TripLegRef",
                    "type": TripLegRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "IndividualPassengerInfoRef",
                    "type": IndividualPassengerInfoRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePoolingDriverInfoRef",
                    "type": VehiclePoolingDriverInfoRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "IndividualTravellerRef",
                    "type": IndividualTravellerRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceAccessCodeRef",
                    "type": ServiceAccessCodeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelDocumentRef",
                    "type": TravelDocumentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RepeatedTripFareRequestRef",
                    "type": RepeatedTripFareRequestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SingleTripFareRequestRef",
                    "type": SingleTripFareRequestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareRequestRef",
                    "type": FareRequestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopFinderRequestRef",
                    "type": StopFinderRequestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopEventRequestRef",
                    "type": StopEventRequestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduleRequestRef",
                    "type": ScheduleRequestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TripPlanRequestRef",
                    "type": TripPlanRequestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerPaymentMeansRef",
                    "type": CustomerPaymentMeansRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ResidentialQualificationEligibilityRef",
                    "type": ResidentialQualificationEligibilityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommercialProfileEligibilityRef",
                    "type": CommercialProfileEligibilityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UserProfileEligibilityRef",
                    "type": UserProfileEligibilityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerAccountRef",
                    "type": CustomerAccountRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareContractRef",
                    "type": FareContractRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerRef",
                    "type": CustomerRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleTypeZoneRestrictionRef",
                    "type": VehicleTypeZoneRestrictionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MediumApplicationInstanceRef",
                    "type": MediumApplicationInstanceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MobileDeviceRef",
                    "type": MobileDeviceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EmvCardRef",
                    "type": EmvCardRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SmartcardRef",
                    "type": SmartcardRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StartTimeAtStopPointRef",
                    "type": StartTimeAtStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ResidentialQualificationRef",
                    "type": ResidentialQualificationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfConcessionRef",
                    "type": TypeOfConcessionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfUsageParameterRef",
                    "type": TypeOfUsageParameterRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ZoneInSeriesRef",
                    "type": ZoneInSeriesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TariffObjectRef",
                    "type": TariffObjectRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "TypeOfFareTableRef",
                    "type": TypeOfFareTableRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareTableRowRef",
                    "type": FareTableRowRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareTableColumnRef",
                    "type": FareTableColumnRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeUnitRef",
                    "type": TimeUnitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalUnitRef",
                    "type": GeographicalUnitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControllableElementInSequenceRef",
                    "type": ControllableElementInSequenceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElementInSequenceRef",
                    "type": FareStructureElementInSequenceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessRightInProductRef",
                    "type": AccessRightInProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CellRef",
                    "type": CellRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerPurchasePackagePriceRef",
                    "type": CustomerPurchasePackagePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPriceRef",
                    "type": ParkingPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeIntervalPriceRef",
                    "type": TimeIntervalPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeUnitPriceRef",
                    "type": TimeUnitPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QualityStructureFactorPriceRef",
                    "type": QualityStructureFactorPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControllableElementPriceRef",
                    "type": ControllableElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidableElementPriceRef",
                    "type": ValidableElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalIntervalPriceRef",
                    "type": GeographicalIntervalPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalUnitPriceRef",
                    "type": GeographicalUnitPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageParameterPriceRef",
                    "type": UsageParameterPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeriesConstraintPriceRef",
                    "type": SeriesConstraintPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackagePriceRef",
                    "type": SalesOfferPackagePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElementPriceRef",
                    "type": DistanceMatrixElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElementPriceRef",
                    "type": FareStructureElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FulfilmentMethodPriceRef",
                    "type": FulfilmentMethodPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappingRulePriceRef",
                    "type": CappingRulePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareProductPriceRef",
                    "type": FareProductPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FarePriceRef",
                    "type": FarePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerPurchasePackageElementRef",
                    "type": CustomerPurchasePackageElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerPurchasePackageRef",
                    "type": CustomerPurchasePackageRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControllableElementRef",
                    "type": ControllableElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidableElementRef",
                    "type": ValidableElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AdditionalDriverOptionRef",
                    "type": AdditionalDriverOptionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RentalOptionRef",
                    "type": RentalOptionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RentalPenaltyPolicyRef",
                    "type": RentalPenaltyPolicyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageEntitlementGivenRef",
                    "type": SalesOfferPackageEntitlementGivenRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageEntitlementRequiredRef",
                    "type": SalesOfferPackageEntitlementRequiredRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MinimumStayRef",
                    "type": MinimumStayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "InterchangingRef",
                    "type": InterchangingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FrequencyOfUseRef",
                    "type": FrequencyOfUseRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SuspendingRef",
                    "type": SuspendingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageValidityPeriodRef",
                    "type": UsageValidityPeriodRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StepLimitRef",
                    "type": StepLimitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoutingRef",
                    "type": RoutingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoundTripRef",
                    "type": RoundTripRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LuggageAllowanceRef",
                    "type": LuggageAllowanceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntitlementGivenRef",
                    "type": EntitlementGivenRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntitlementRequiredRef",
                    "type": EntitlementRequiredRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EligibilityChangePolicyRef",
                    "type": EligibilityChangePolicyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupTicketRef",
                    "type": GroupTicketRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommercialProfileRef",
                    "type": CommercialProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePoolerProfileRef",
                    "type": VehiclePoolerProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompanionProfileRef",
                    "type": CompanionProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UserProfileRef",
                    "type": UserProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ProfileParameterRef",
                    "type": ProfileParameterRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SubscribingRef",
                    "type": SubscribingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PenaltyPolicyRef",
                    "type": PenaltyPolicyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChargingPolicyRef",
                    "type": ChargingPolicyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransferabilityRef",
                    "type": TransferabilityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReplacingRef",
                    "type": ReplacingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RefundingRef",
                    "type": RefundingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ExchangingRef",
                    "type": ExchangingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ResellingRef",
                    "type": ResellingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CancellingRef",
                    "type": CancellingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReservingRef",
                    "type": ReservingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BookingPolicyRef",
                    "type": BookingPolicyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PurchaseWindowRef",
                    "type": PurchaseWindowRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeriesConstraintRef",
                    "type": SeriesConstraintRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageElementRef",
                    "type": SalesOfferPackageElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageRef",
                    "type": SalesOfferPackageRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElementInverseRef",
                    "type": DistanceMatrixElementInverseRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElementRef",
                    "type": DistanceMatrixElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElementRef",
                    "type": FareStructureElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FulfilmentMethodRef",
                    "type": FulfilmentMethodRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappingRuleRef",
                    "type": CappingRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntitlementProductRef",
                    "type": EntitlementProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SupplementProductRef",
                    "type": SupplementProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PreassignedFareProductRef",
                    "type": PreassignedFareProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AmountOfPriceUnitProductRef",
                    "type": AmountOfPriceUnitProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageDiscountRightRef",
                    "type": UsageDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ThirdPartyProductRef",
                    "type": ThirdPartyProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappedDiscountRightRef",
                    "type": CappedDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SaleDiscountRightRef",
                    "type": SaleDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareProductRef",
                    "type": FareProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceAccessRightRef",
                    "type": ServiceAccessRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeIntervalRef",
                    "type": TimeIntervalRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalIntervalRef",
                    "type": GeographicalIntervalRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingChargeBandRef",
                    "type": ParkingChargeBandRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeStructureFactorRef",
                    "type": TimeStructureFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareQuotaFactorRef",
                    "type": FareQuotaFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareDemandFactorRef",
                    "type": FareDemandFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QualityStructureFactorRef",
                    "type": QualityStructureFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalStructureFactorRef",
                    "type": GeographicalStructureFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PriceableObjectRef",
                    "type": PriceableObjectRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MonthValidityOffsetRef",
                    "type": MonthValidityOffsetRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "PricingServiceRef",
                    "type": PricingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoundingStepRef",
                    "type": RoundingStepRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoundingRef",
                    "type": RoundingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PricingParameterSetRef",
                    "type": PricingParameterSetRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RechargingStepRef",
                    "type": RechargingStepRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RechargingPlanRef",
                    "type": RechargingPlanRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleServicePropertiesRef",
                    "type": FlexibleServicePropertiesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DriverTripTimeRef",
                    "type": DriverTripTimeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DriverTripRef",
                    "type": DriverTripRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DutyPartRef",
                    "type": DutyPartRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccountableElementRef",
                    "type": AccountableElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DutyRef",
                    "type": DutyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReliefOpportunityRef",
                    "type": ReliefOpportunityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CourseOfJourneysRef",
                    "type": CourseOfJourneysRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DriverRef",
                    "type": DriverRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleServicePartRef",
                    "type": VehicleServicePartRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleServiceRef",
                    "type": VehicleServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompoundBlockRef",
                    "type": CompoundBlockRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainBlockPartRef",
                    "type": TrainBlockPartRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BlockPartRef",
                    "type": BlockPartRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainBlockRef",
                    "type": TrainBlockRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BlockRef",
                    "type": BlockRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPartCoupleRef",
                    "type": JourneyPartCoupleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CoupledJourneyRef",
                    "type": CoupledJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPartRef",
                    "type": JourneyPartRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "InterchangeRuleTimingRef",
                    "type": InterchangeRuleTimingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "InterchangeRuleRef",
                    "type": InterchangeRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyPatternInterchangeRef",
                    "type": ServiceJourneyPatternInterchangeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyInterchangeRef",
                    "type": ServiceJourneyInterchangeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DefaultInterchangeRef",
                    "type": DefaultInterchangeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "InterchangeRef",
                    "type": InterchangeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyMeetingRef",
                    "type": JourneyMeetingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerAtStopTimeRef",
                    "type": PassengerAtStopTimeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimetabledPassingTimeRef",
                    "type": TimetabledPassingTimeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EstimatedPassingTimeRef",
                    "type": EstimatedPassingTimeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ObservedPassingTimeRef",
                    "type": ObservedPassingTimeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TargetPassingTimeRef",
                    "type": TargetPassingTimeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainNumberRef",
                    "type": TrainNumberRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoutingConstraintZoneRef",
                    "type": RoutingConstraintZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePositionAlignmentRef",
                    "type": VehiclePositionAlignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleQuayAlignmentRef",
                    "type": VehicleQuayAlignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LogicalDisplayRef",
                    "type": LogicalDisplayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPropertiesRef",
                    "type": ParkingPropertiesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingCapacityRef",
                    "type": ParkingCapacityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineNetworkRef",
                    "type": LineNetworkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RouteInstructionRef",
                    "type": RouteInstructionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexiblePointPropertiesRef",
                    "type": FlexiblePointPropertiesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleLinkPropertiesRef",
                    "type": FlexibleLinkPropertiesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeDemandProfileRef",
                    "type": TimeDemandProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeDemandTypeRef",
                    "type": TimeDemandTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleTypePreferenceRef",
                    "type": VehicleTypePreferenceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternHeadwayRef",
                    "type": JourneyPatternHeadwayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternLayoverRef",
                    "type": JourneyPatternLayoverRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternRunTimeRef",
                    "type": JourneyPatternRunTimeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternWaitTimeRef",
                    "type": JourneyPatternWaitTimeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DefaultServiceJourneyTimeRef",
                    "type": DefaultServiceJourneyTimeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DefaultDeadRunRunTimeRef",
                    "type": DefaultDeadRunRunTimeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TurnaroundTimeLimitTimeRef",
                    "type": TurnaroundTimeLimitTimeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyTimingRef",
                    "type": JourneyTimingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CrewBaseRef",
                    "type": CrewBaseRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RollingStockInventoryRef",
                    "type": RollingStockInventoryRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrailingRollingStockItemRef",
                    "type": TrailingRollingStockItemRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TractiveRollingStockItemRef",
                    "type": TractiveRollingStockItemRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleRef",
                    "type": VehicleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SpotAffinityRef",
                    "type": SpotAffinityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainComponentRef",
                    "type": TrainComponentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainElementRef",
                    "type": TrainElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrailingElementTypeRef",
                    "type": TrailingElementTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TractiveElementTypeRef",
                    "type": TractiveElementTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainElementTypeRef",
                    "type": TrainElementTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainInCompoundTrainRef",
                    "type": TrainInCompoundTrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerSeatRef",
                    "type": PassengerSeatRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelDocumentSecurityListingRef",
                    "type": TravelDocumentSecurityListingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RetailDeviceSecurityListingRef",
                    "type": RetailDeviceSecurityListingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerAccountSecurityListingRef",
                    "type": CustomerAccountSecurityListingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareContractSecurityListingRef",
                    "type": FareContractSecurityListingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerSecurityListingRef",
                    "type": CustomerSecurityListingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MediumAccessDeviceSecurityListingRef",
                    "type": MediumAccessDeviceSecurityListingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WhitelistRef",
                    "type": WhitelistRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BlacklistRef",
                    "type": BlacklistRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SchematicMapMemberRef",
                    "type": SchematicMapMemberRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SchematicMapRef",
                    "type": SchematicMapRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "DeckSpaceCapacityRef",
                    "type": DeckSpaceCapacityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeckLevelRef",
                    "type": DeckLevelRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeckEntranceCoupleRef",
                    "type": DeckEntranceCoupleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeckEntranceUsageRef",
                    "type": DeckEntranceUsageRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeckRef",
                    "type": DeckRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeckPlanRef",
                    "type": DeckPlanRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeckWindowRef",
                    "type": DeckWindowRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OtherDeckEntranceRef",
                    "type": OtherDeckEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeckVehicleEntranceRef",
                    "type": DeckVehicleEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerEntranceRef",
                    "type": PassengerEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "SpotColumnRef",
                    "type": SpotColumnRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SpotRowRef",
                    "type": SpotRowRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SensorInEntranceRef",
                    "type": SensorInEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SensorInSpotRef",
                    "type": SensorInSpotRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ModeRestrictionAssessmentRef",
                    "type": ModeRestrictionAssessmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeliveryVariantRef",
                    "type": DeliveryVariantRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NoticeRef",
                    "type": NoticeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleEquipmentProfileMemberRef",
                    "type": VehicleEquipmentProfileMemberRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleProfileRef",
                    "type": VehicleProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RechargingEquipmentProfileRef",
                    "type": RechargingEquipmentProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleEquipmentProfileRef",
                    "type": VehicleEquipmentProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleModelRef",
                    "type": VehicleModelRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerVehicleCapacityRef",
                    "type": PassengerVehicleCapacityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerCapacityRef",
                    "type": PassengerCapacityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FacilityRequirementRef",
                    "type": FacilityRequirementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleManoeuvringRequirementRef",
                    "type": VehicleManoeuvringRequirementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerCarryingRequirementRef",
                    "type": PassengerCarryingRequirementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleRequirementRef",
                    "type": VehicleRequirementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "OnboardStayRef",
                    "type": OnboardStayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccommodationRef",
                    "type": AccommodationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "FacilityRef",
                    "type": FacilityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatingDepartmentRef",
                    "type": OperatingDepartmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperationalContextRef",
                    "type": OperationalContextRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LevelInStructureRef",
                    "type": LevelInStructureRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteStructureRef",
                    "type": SiteStructureRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LevelRef",
                    "type": LevelRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ModeRef",
                    "type": ModeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SubmodeRef",
                    "type": SubmodeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OpenTransportModeRef",
                    "type": OpenTransportModeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PathInstructionRef",
                    "type": PathInstructionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OffenceDebitRef",
                    "type": OffenceDebitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareProductSaleDebitRef",
                    "type": FareProductSaleDebitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TripDebitRef",
                    "type": TripDebitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BookingDebitRef",
                    "type": BookingDebitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OtherDebitRef",
                    "type": OtherDebitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareDebitRef",
                    "type": FareDebitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesTransactionRef",
                    "type": SalesTransactionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OfferedTravelSpecificationRef",
                    "type": OfferedTravelSpecificationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RequestedTravelSpecificationRef",
                    "type": RequestedTravelSpecificationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelSpecificationRef",
                    "type": TravelSpecificationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareContractEntryRef",
                    "type": FareContractEntryRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LogEntryRef",
                    "type": LogEntryRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimebandRef",
                    "type": TimebandRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareDayTypeRef",
                    "type": FareDayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DayTypeRef",
                    "type": DayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DefaultConnectionRef",
                    "type": DefaultConnectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteConnectionRef",
                    "type": SiteConnectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ConnectionRef",
                    "type": ConnectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessRef",
                    "type": AccessRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HailAndRideAreaRef",
                    "type": HailAndRideAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleAreaRef",
                    "type": FlexibleAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleQuayRef",
                    "type": FlexibleQuayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleStopPlaceRef",
                    "type": FlexibleStopPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EquipmentPlaceRef",
                    "type": EquipmentPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EquipmentPositionRef",
                    "type": EquipmentPositionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TopographicPlaceRef",
                    "type": TopographicPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "GarageRef",
                    "type": GarageRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "AddressablePlaceRef",
                    "type": AddressablePlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "DeckPathJunctionRef",
                    "type": DeckPathJunctionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PathJunctionRef",
                    "type": PathJunctionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SitePathJunctionRef",
                    "type": SitePathJunctionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GenericPathJunctionRef",
                    "type": GenericPathJunctionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UicOperatingPeriodRef",
                    "type": UicOperatingPeriodRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatingPeriodRef",
                    "type": OperatingPeriodRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatingDayRef",
                    "type": OperatingDayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceCalendarRef",
                    "type": ServiceCalendarRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ContactRef",
                    "type": ContactRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TopographicProjectionRef",
                    "type": TopographicProjectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ComplexFeatureProjectionRef",
                    "type": ComplexFeatureProjectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LinkSequenceProjectionRef",
                    "type": LinkSequenceProjectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ZoneProjectionRef",
                    "type": ZoneProjectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LinkProjectionRef",
                    "type": LinkProjectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointProjectionRef",
                    "type": PointProjectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TripRef",
                    "type": TripRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TripPatternTripRef",
                    "type": TripPatternTripRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SingleJourneyPathRef",
                    "type": SingleJourneyPathRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SingleJourneyRef",
                    "type": SingleJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NormalDatedVehicleJourneyRef",
                    "type": NormalDatedVehicleJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DatedVehicleJourneyRef",
                    "type": DatedVehicleJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DatedSpecialServiceRef",
                    "type": DatedSpecialServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SpecialServiceRef",
                    "type": SpecialServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "DeadRunRef",
                    "type": DeadRunRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleJourneyRef",
                    "type": VehicleJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyPatternRef",
                    "type": ServiceJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServicePatternRef",
                    "type": ServicePatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRunJourneyPatternRef",
                    "type": DeadRunJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternRef",
                    "type": JourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingPatternRef",
                    "type": TimingPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RouteRef",
                    "type": RouteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeckNavigationPathRef",
                    "type": DeckNavigationPathRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NavigationPathRef",
                    "type": NavigationPathRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteNavigationPathRef",
                    "type": SiteNavigationPathRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GenericNavigationPathRef",
                    "type": GenericNavigationPathRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LinkSequenceRef",
                    "type": LinkSequenceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OnwardVehicleMeetingLinkRef",
                    "type": OnwardVehicleMeetingLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleMeetingLinkRef",
                    "type": VehicleMeetingLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceLinkRef",
                    "type": ServiceLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineLinkRef",
                    "type": LineLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingLinkRef",
                    "type": TimingLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WireLinkRef",
                    "type": WireLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadLinkRef",
                    "type": RoadLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RailwayLinkRef",
                    "type": RailwayLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActivationLinkRef",
                    "type": ActivationLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RouteLinkRef",
                    "type": RouteLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeckPathLinkRef",
                    "type": DeckPathLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OffSitePathLinkRef",
                    "type": OffSitePathLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PathLinkRef",
                    "type": PathLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SitePathLinkRef",
                    "type": SitePathLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GenericPathLinkRef",
                    "type": GenericPathLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleMeetingPointRef",
                    "type": VehicleMeetingPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WirePointRef",
                    "type": WirePointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadPointRef",
                    "type": RoadPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RailwayPointRef",
                    "type": RailwayPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrafficControlPointRef",
                    "type": TrafficControlPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BeaconPointRef",
                    "type": BeaconPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActivationPointRef",
                    "type": ActivationPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BorderPointRef",
                    "type": BorderPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "GaragePointRef",
                    "type": GaragePointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPointRef",
                    "type": ParkingPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReliefPointRef",
                    "type": ReliefPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingPointRef",
                    "type": TimingPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoutePointRef",
                    "type": RoutePointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointRef",
                    "type": PointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ResponsibilityRoleRef",
                    "type": ResponsibilityRoleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AlternativeNameRef",
                    "type": AlternativeNameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AlternativeTextRef",
                    "type": AlternativeTextRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AvailabilityConditionRef",
                    "type": AvailabilityConditionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityRuleParameterRef",
                    "type": ValidityRuleParameterRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityTriggerRef",
                    "type": ValidityTriggerRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityConditionRef",
                    "type": ValidityConditionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControlCentreRef",
                    "type": ControlCentreRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationalUnitRef",
                    "type": OrganisationalUnitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DepartmentRef",
                    "type": DepartmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationPartRef",
                    "type": OrganisationPartRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "ResponsibilitySetRef",
                    "type": ResponsibilitySetRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DestinationDisplayVariantRef",
                    "type": DestinationDisplayVariantRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DestinationDisplayRef",
                    "type": DestinationDisplayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AllowedLineDirectionRef",
                    "type": AllowedLineDirectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "GroupOfCustomerPurchasePackagesRef",
                    "type": GroupOfCustomerPurchasePackagesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PoolOfVehiclesRef",
                    "type": PoolOfVehiclesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfSalesOfferPackagesRef",
                    "type": GroupOfSalesOfferPackagesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfDistanceMatrixElementsRef",
                    "type": GroupOfDistanceMatrixElementsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfDistributionChannelsRef",
                    "type": GroupOfDistributionChannelsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfSingleJourneysRef",
                    "type": GroupOfSingleJourneysRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StandardFareTableRef",
                    "type": StandardFareTableRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareTableRef",
                    "type": FareTableRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PriceGroupRef",
                    "type": PriceGroupRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RhythmicalJourneyGroupRef",
                    "type": RhythmicalJourneyGroupRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HeadwayJourneyGroupRef",
                    "type": HeadwayJourneyGroupRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyFrequencyGroupRef",
                    "type": JourneyFrequencyGroupRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfServicesRef",
                    "type": GroupOfServicesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestHierarchyRef",
                    "type": PointOfInterestHierarchyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfTimingLinksRef",
                    "type": GroupOfTimingLinksRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FleetRef",
                    "type": FleetRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfStopPlacesRef",
                    "type": GroupOfStopPlacesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfOperatorsRef",
                    "type": GroupOfOperatorsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfSitesRef",
                    "type": GroupOfSitesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfPlacesRef",
                    "type": GroupOfPlacesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParentSectionRef",
                    "type": ParentSectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParentCommonSectionRef",
                    "type": ParentCommonSectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommonSectionRef",
                    "type": CommonSectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineSectionRef",
                    "type": LineSectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareSectionRef",
                    "type": FareSectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralSectionRef",
                    "type": GeneralSectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SectionRef",
                    "type": SectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LogRef",
                    "type": LogRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfTimebandsRef",
                    "type": GroupOfTimebandsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PlaceRef",
                    "type": PlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfTariffZonesRef",
                    "type": GroupOfTariffZonesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MobilityServiceConstraintZoneRef",
                    "type": MobilityServiceConstraintZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopAreaRef",
                    "type": StopAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransportAdministrativeZoneRef",
                    "type": TransportAdministrativeZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessZoneRef",
                    "type": AccessZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AdministrativeZoneRef",
                    "type": AdministrativeZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "ZoneRef",
                    "type": ZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LayerRef",
                    "type": LayerRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "GeneralGroupOfEntitiesRef",
                    "type": GeneralGroupOfEntitiesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MobilityJourneyFrameRef",
                    "type": MobilityJourneyFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MobilityServiceFrameRef",
                    "type": MobilityServiceFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesTransactionFrameRef",
                    "type": SalesTransactionFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareFrameRef",
                    "type": FareFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceFrameRef",
                    "type": ServiceFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DriverScheduleFrameRef",
                    "type": DriverScheduleFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleScheduleFrameRef",
                    "type": VehicleScheduleFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimetableFrameRef",
                    "type": TimetableFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteFrameRef",
                    "type": SiteFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "InfrastructureFrameRef",
                    "type": InfrastructureFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralFrameRef",
                    "type": GeneralFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ResourceFrameRef",
                    "type": ResourceFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceCalendarFrameRef",
                    "type": ServiceCalendarFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompositeFrameRef",
                    "type": CompositeFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingBayConditionRef",
                    "type": ParkingBayConditionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RentalAvailabilityRef",
                    "type": RentalAvailabilityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingBayStatusRef",
                    "type": ParkingBayStatusRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfMediumAccessDeviceRef",
                    "type": TypeOfMediumAccessDeviceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfProofRef",
                    "type": TypeOfProofRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistributionChannelRef",
                    "type": DistributionChannelRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChargingMomentRef",
                    "type": ChargingMomentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PriceUnitRef",
                    "type": PriceUnitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PurposeOfJourneyPartitionRef",
                    "type": PurposeOfJourneyPartitionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingAlgorithmTypeRef",
                    "type": TimingAlgorithmTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfParkingRef",
                    "type": TypeOfParkingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestClassificationRef",
                    "type": PointOfInterestClassificationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfActivationRef",
                    "type": TypeOfActivationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFleetRef",
                    "type": TypeOfFleetRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfDeckEntranceRef",
                    "type": TypeOfDeckEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfDeckSpaceRef",
                    "type": TypeOfDeckSpaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfLocatableSpotRef",
                    "type": TypeOfLocatableSpotRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DirectionRef",
                    "type": DirectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfDriverPermitRef",
                    "type": TypeOfDriverPermitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AcceptedDriverPermitRef",
                    "type": AcceptedDriverPermitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PurposeOfEquipmentProfileRef",
                    "type": PurposeOfEquipmentProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfProductCategoryRef",
                    "type": TypeOfProductCategoryRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPaymentMethodRef",
                    "type": TypeOfPaymentMethodRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ClassOfUseRef",
                    "type": ClassOfUseRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfOperationRef",
                    "type": TypeOfOperationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfCodespaceAssignmentRef",
                    "type": TypeOfCodespaceAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BrandingRef",
                    "type": BrandingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfResponsibilityRoleRef",
                    "type": TypeOfResponsibilityRoleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PurposeOfGroupingRef",
                    "type": PurposeOfGroupingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfRetailDeviceRef",
                    "type": TypeOfRetailDeviceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerAccountStatusRef",
                    "type": CustomerAccountStatusRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfCustomerAccountRef",
                    "type": TypeOfCustomerAccountRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareContractEntryRef",
                    "type": TypeOfFareContractEntryRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareContractRef",
                    "type": TypeOfFareContractRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfAccessRightAssignmentRef",
                    "type": TypeOfAccessRightAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfSalesOfferPackageRef",
                    "type": TypeOfSalesOfferPackageRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareStructureElementRef",
                    "type": TypeOfFareStructureElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTariffRef",
                    "type": TypeOfTariffRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AllDistributionChannelsRef",
                    "type": AllDistributionChannelsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfMachineReadabilityRef",
                    "type": TypeOfMachineReadabilityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTravelDocumentRef",
                    "type": TypeOfTravelDocumentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfMobilityServiceRef",
                    "type": TypeOfMobilityServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareProductRef",
                    "type": TypeOfFareProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareStructureFactorRef",
                    "type": TypeOfFareStructureFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPricingRuleRef",
                    "type": TypeOfPricingRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFlexibleServiceRef",
                    "type": TypeOfFlexibleServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPassengerInformationEquipmentRef",
                    "type": TypeOfPassengerInformationEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTimeDemandTypeRef",
                    "type": TypeOfTimeDemandTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfJourneyPatternRef",
                    "type": TypeOfJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfRollingStockRef",
                    "type": TypeOfRollingStockRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfSecurityListRef",
                    "type": TypeOfSecurityListRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPlugRef",
                    "type": TypeOfPlugRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfBatteryChemistryRef",
                    "type": TypeOfBatteryChemistryRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfServiceFeatureRef",
                    "type": TypeOfServiceFeatureRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfDeliveryVariantRef",
                    "type": TypeOfDeliveryVariantRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfNoticeRef",
                    "type": TypeOfNoticeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfCongestionRef",
                    "type": TypeOfCongestionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfServiceRef",
                    "type": TypeOfServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFacilityRef",
                    "type": TypeOfFacilityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfModeOfOperationRef",
                    "type": TypeOfModeOfOperationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "TypeOfEquipmentRef",
                    "type": TypeOfEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPlaceRef",
                    "type": TypeOfPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTransferRef",
                    "type": TypeOfTransferRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfOrganisationPartRef",
                    "type": TypeOfOrganisationPartRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfOrganisationRef",
                    "type": TypeOfOrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfZoneRef",
                    "type": TypeOfZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfProjectionRef",
                    "type": TypeOfProjectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFeatureRef",
                    "type": TypeOfFeatureRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfLinkSequenceRef",
                    "type": TypeOfLinkSequenceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfLinkRef",
                    "type": TypeOfLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPointRef",
                    "type": TypeOfPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfLineRef",
                    "type": TypeOfLineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfValidityRef",
                    "type": TypeOfValidityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFrameRef",
                    "type": TypeOfFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DataSourceRef",
                    "type": DataSourceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VersionRef",
                    "type": VersionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VersionOfObjectRef",
                    "type": VersionOfObjectRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    hide: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Hide",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    display_as_icon: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DisplayAsIcon",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    info_link: Optional[InfoLink] = field(
        default=None,
        metadata={
            "name": "InfoLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    x: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    y: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    projection: Optional[Union[TopographicProjection, ZoneProjection, ComplexFeatureProjection, LinkSequenceProjection, LinkProjection, PointProjection]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TopographicProjection",
                    "type": TopographicProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ZoneProjection",
                    "type": ZoneProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ComplexFeatureProjection",
                    "type": ComplexFeatureProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LinkSequenceProjection",
                    "type": LinkSequenceProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LinkProjection",
                    "type": LinkProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointProjection",
                    "type": PointProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
