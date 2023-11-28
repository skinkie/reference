from dataclasses import dataclass, field
from typing import Optional
from netex.access_ref import AccessRef
from netex.access_right_in_product_ref import AccessRightInProductRef
from netex.access_space_ref import AccessSpaceRef
from netex.access_zone_ref import AccessZoneRef
from netex.accommodation_ref import AccommodationRef
from netex.accountable_element_ref import AccountableElementRef
from netex.activation_link_ref import ActivationLinkRef
from netex.activation_point_ref import ActivationPointRef
from netex.additional_driver_option_ref import AdditionalDriverOptionRef
from netex.address_ref import AddressRef
from netex.addressable_place_ref import AddressablePlaceRef
from netex.administrative_zone_ref import AdministrativeZoneRef
from netex.all_authorities_ref import AllAuthoritiesRef
from netex.all_distribution_channels_ref import AllDistributionChannelsRef
from netex.all_operators_ref import AllOperatorsRef
from netex.all_organisations_ref import AllOrganisationsRef
from netex.all_public_transport_organisations_ref import AllPublicTransportOrganisationsRef
from netex.all_transport_organisations_ref import AllTransportOrganisationsRef
from netex.allowed_line_direction_ref import AllowedLineDirectionRef
from netex.alternative_name_ref import AlternativeNameRef
from netex.alternative_text_ref import AlternativeTextRef
from netex.alternative_texts_rel_structure import VersionedChildStructure
from netex.amount_of_price_unit_product_ref import AmountOfPriceUnitProductRef
from netex.authority_ref import AuthorityRef
from netex.availability_condition_ref import AvailabilityConditionRef
from netex.beacon_point_ref import BeaconPointRef
from netex.blacklist_ref import BlacklistRef
from netex.block_part_ref import BlockPartRef
from netex.block_ref import BlockRef
from netex.boarding_position_ref import BoardingPositionRef
from netex.booking_policy_ref import BookingPolicyRef
from netex.border_point_ref import BorderPointRef
from netex.branding_ref import BrandingRef
from netex.cancelling_ref import CancellingRef
from netex.capped_discount_right_ref import CappedDiscountRightRef
from netex.capping_rule_price_ref import CappingRulePriceRef
from netex.capping_rule_ref import CappingRuleRef
from netex.car_model_profile_ref import CarModelProfileRef
from netex.cell_ref import CellRef
from netex.charging_equipment_profile_ref import ChargingEquipmentProfileRef
from netex.charging_moment_ref import ChargingMomentRef
from netex.charging_policy_ref import ChargingPolicyRef
from netex.class_of_use_ref import ClassOfUseRef
from netex.commercial_profile_eligibility_ref import CommercialProfileEligibilityRef
from netex.commercial_profile_ref import CommercialProfileRef
from netex.common_section_ref import CommonSectionRef
from netex.companion_profile_ref import CompanionProfileRef
from netex.complex_feature_projection import ComplexFeatureProjection
from netex.complex_feature_projection_ref import ComplexFeatureProjectionRef
from netex.composite_frame_ref import CompositeFrameRef
from netex.compound_block_ref import CompoundBlockRef
from netex.compound_train_ref import CompoundTrainRef
from netex.connection_ref import ConnectionRef
from netex.contact_ref import ContactRef
from netex.control_centre_ref import ControlCentreRef
from netex.controllable_element_in_sequence_ref import ControllableElementInSequenceRef
from netex.controllable_element_price_ref import ControllableElementPriceRef
from netex.controllable_element_ref import ControllableElementRef
from netex.coupled_journey_ref import CoupledJourneyRef
from netex.course_of_journeys_ref import CourseOfJourneysRef
from netex.crew_base_ref import CrewBaseRef
from netex.customer_account_ref import CustomerAccountRef
from netex.customer_account_security_listing_ref import CustomerAccountSecurityListingRef
from netex.customer_account_status_ref import CustomerAccountStatusRef
from netex.customer_payment_means_ref import CustomerPaymentMeansRef
from netex.customer_purchase_package_element_ref import CustomerPurchasePackageElementRef
from netex.customer_purchase_package_price_ref import CustomerPurchasePackagePriceRef
from netex.customer_purchase_package_ref import CustomerPurchasePackageRef
from netex.customer_ref import CustomerRef
from netex.customer_security_listing_ref import CustomerSecurityListingRef
from netex.cycle_model_profile_ref import CycleModelProfileRef
from netex.data_source_ref import DataSourceRef
from netex.dated_special_service_ref import DatedSpecialServiceRef
from netex.dated_vehicle_journey_ref import DatedVehicleJourneyRef
from netex.day_type_ref import DayTypeRef
from netex.dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from netex.dead_run_ref import DeadRunRef
from netex.default_connection_ref import DefaultConnectionRef
from netex.default_dead_run_run_time_ref import DefaultDeadRunRunTimeRef
from netex.default_interchange_ref import DefaultInterchangeRef
from netex.default_service_journey_time_ref import DefaultServiceJourneyTimeRef
from netex.delivery_variant_ref import DeliveryVariantRef
from netex.department_ref import DepartmentRef
from netex.destination_display_ref import DestinationDisplayRef
from netex.destination_display_variant_ref import DestinationDisplayVariantRef
from netex.direction_ref import DirectionRef
from netex.discounting_rule_ref import DiscountingRuleRef
from netex.distance_matrix_element_inverse_ref import DistanceMatrixElementInverseRef
from netex.distance_matrix_element_price_ref import DistanceMatrixElementPriceRef
from netex.distance_matrix_element_ref import DistanceMatrixElementRef
from netex.distribution_channel_ref import DistributionChannelRef
from netex.driver_ref import DriverRef
from netex.driver_schedule_frame_ref import DriverScheduleFrameRef
from netex.driver_trip_ref import DriverTripRef
from netex.driver_trip_time_ref import DriverTripTimeRef
from netex.duty_part_ref import DutyPartRef
from netex.duty_ref import DutyRef
from netex.eligibility_change_policy_ref import EligibilityChangePolicyRef
from netex.emv_card_ref import EmvCardRef
from netex.entitlement_given_ref import EntitlementGivenRef
from netex.entitlement_product_ref import EntitlementProductRef
from netex.entitlement_required_ref import EntitlementRequiredRef
from netex.entrance_ref import EntranceRef
from netex.equipment_place_ref import EquipmentPlaceRef
from netex.equipment_position_ref import EquipmentPositionRef
from netex.estimated_passing_time_ref import EstimatedPassingTimeRef
from netex.exchanging_ref import ExchangingRef
from netex.facility_ref import FacilityRef
from netex.facility_requirement_ref import FacilityRequirementRef
from netex.facility_set_ref import FacilitySetRef
from netex.fare_contract_entry_ref import FareContractEntryRef
from netex.fare_contract_ref import FareContractRef
from netex.fare_contract_security_listing_ref import FareContractSecurityListingRef
from netex.fare_day_type_ref import FareDayTypeRef
from netex.fare_demand_factor_ref import FareDemandFactorRef
from netex.fare_frame_ref import FareFrameRef
from netex.fare_price_ref import FarePriceRef
from netex.fare_product_price_ref import FareProductPriceRef
from netex.fare_product_ref import FareProductRef
from netex.fare_quota_factor_ref import FareQuotaFactorRef
from netex.fare_request_ref import FareRequestRef
from netex.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from netex.fare_section_ref import FareSectionRef
from netex.fare_structure_element_in_sequence_ref import FareStructureElementInSequenceRef
from netex.fare_structure_element_price_ref import FareStructureElementPriceRef
from netex.fare_structure_element_ref import FareStructureElementRef
from netex.fare_table_column_ref import FareTableColumnRef
from netex.fare_table_ref import FareTableRef
from netex.fare_table_row_ref import FareTableRowRef
from netex.fare_zone_ref import FareZoneRef
from netex.fleet_ref import FleetRef
from netex.flexible_area_ref import FlexibleAreaRef
from netex.flexible_line_ref import FlexibleLineRef
from netex.flexible_link_properties_ref import FlexibleLinkPropertiesRef
from netex.flexible_mode_of_operation_ref import FlexibleModeOfOperationRef
from netex.flexible_point_properties_ref import FlexiblePointPropertiesRef
from netex.flexible_quay_ref import FlexibleQuayRef
from netex.flexible_service_properties_ref import FlexibleServicePropertiesRef
from netex.flexible_stop_place_ref import FlexibleStopPlaceRef
from netex.frequency_of_use_ref import FrequencyOfUseRef
from netex.fulfilment_method_price_ref import FulfilmentMethodPriceRef
from netex.fulfilment_method_ref import FulfilmentMethodRef
from netex.garage_point_ref import GaragePointRef
from netex.garage_ref import GarageRef
from netex.general_frame_ref import GeneralFrameRef
from netex.general_group_of_entities_ref import GeneralGroupOfEntitiesRef
from netex.general_organisation_ref import GeneralOrganisationRef
from netex.general_section_ref import GeneralSectionRef
from netex.geographical_interval_price_ref import GeographicalIntervalPriceRef
from netex.geographical_interval_ref import GeographicalIntervalRef
from netex.geographical_structure_factor_ref import GeographicalStructureFactorRef
from netex.geographical_unit_price_ref import GeographicalUnitPriceRef
from netex.geographical_unit_ref import GeographicalUnitRef
from netex.group_of_customer_purchase_packages_ref import GroupOfCustomerPurchasePackagesRef
from netex.group_of_distance_matrix_elements_ref import GroupOfDistanceMatrixElementsRef
from netex.group_of_distribution_channels_ref import GroupOfDistributionChannelsRef
from netex.group_of_lines_ref import GroupOfLinesRef
from netex.group_of_operators_ref import GroupOfOperatorsRef
from netex.group_of_places_ref import GroupOfPlacesRef
from netex.group_of_sales_offer_packages_ref import GroupOfSalesOfferPackagesRef
from netex.group_of_services_ref import GroupOfServicesRef
from netex.group_of_single_journeys_ref import GroupOfSingleJourneysRef
from netex.group_of_stop_places_ref import GroupOfStopPlacesRef
from netex.group_of_timebands_ref import GroupOfTimebandsRef
from netex.group_of_timing_links_ref import GroupOfTimingLinksRef
from netex.group_ticket_ref import GroupTicketRef
from netex.hail_and_ride_area_ref import HailAndRideAreaRef
from netex.headway_journey_group_ref import HeadwayJourneyGroupRef
from netex.individual_passenger_info_ref import IndividualPassengerInfoRef
from netex.individual_traveller_ref import IndividualTravellerRef
from netex.info_link import InfoLink
from netex.infrastructure_frame_ref import InfrastructureFrameRef
from netex.interchange_ref import InterchangeRef
from netex.interchange_rule_ref import InterchangeRuleRef
from netex.interchange_rule_timing_ref import InterchangeRuleTimingRef
from netex.interchanging_ref import InterchangingRef
from netex.journey_frequency_group_ref import JourneyFrequencyGroupRef
from netex.journey_meeting_ref import JourneyMeetingRef
from netex.journey_part_couple_ref import JourneyPartCoupleRef
from netex.journey_part_ref import JourneyPartRef
from netex.journey_pattern_headway_ref import JourneyPatternHeadwayRef
from netex.journey_pattern_layover_ref import JourneyPatternLayoverRef
from netex.journey_pattern_ref import JourneyPatternRef
from netex.journey_pattern_run_time_ref import JourneyPatternRunTimeRef
from netex.journey_pattern_wait_time_ref import JourneyPatternWaitTimeRef
from netex.journey_timing_ref import JourneyTimingRef
from netex.layer_ref import LayerRef
from netex.level_ref import LevelRef
from netex.limiting_rule_ref import LimitingRuleRef
from netex.line_link_ref import LineLinkRef
from netex.line_network_ref import LineNetworkRef
from netex.line_ref import LineRef
from netex.line_section_ref import LineSectionRef
from netex.link_projection import LinkProjection
from netex.link_projection_ref import LinkProjectionRef
from netex.link_sequence_projection import LinkSequenceProjection
from netex.link_sequence_projection_ref import LinkSequenceProjectionRef
from netex.link_sequence_ref import LinkSequenceRef
from netex.log_entry_ref import LogEntryRef
from netex.log_ref import LogRef
from netex.logical_display_ref import LogicalDisplayRef
from netex.luggage_allowance_ref import LuggageAllowanceRef
from netex.management_agent_ref import ManagementAgentRef
from netex.medium_access_device_security_listing_ref import MediumAccessDeviceSecurityListingRef
from netex.medium_application_instance_ref import MediumApplicationInstanceRef
from netex.minimum_stay_ref import MinimumStayRef
from netex.mobile_device_ref import MobileDeviceRef
from netex.mobility_journey_frame_ref import MobilityJourneyFrameRef
from netex.mobility_service_constraint_zone_ref import MobilityServiceConstraintZoneRef
from netex.mobility_service_frame_ref import MobilityServiceFrameRef
from netex.mode_ref import ModeRef
from netex.mode_restriction_assessment_ref import ModeRestrictionAssessmentRef
from netex.monitored_vehicle_sharing_parking_bay_ref import MonitoredVehicleSharingParkingBayRef
from netex.month_validity_offset_ref import MonthValidityOffsetRef
from netex.multilingual_string import MultilingualString
from netex.navigation_path_ref import NavigationPathRef
from netex.network_ref import NetworkRef
from netex.notice_ref import NoticeRef
from netex.observed_passing_time_ref import ObservedPassingTimeRef
from netex.offered_travel_specification_ref import OfferedTravelSpecificationRef
from netex.onboard_stay_ref import OnboardStayRef
from netex.online_service_operator_ref import OnlineServiceOperatorRef
from netex.onward_vehicle_meeting_link_ref import OnwardVehicleMeetingLinkRef
from netex.open_transport_mode_ref import OpenTransportModeRef
from netex.operating_day_ref import OperatingDayRef
from netex.operating_department_ref import OperatingDepartmentRef
from netex.operating_period_ref import OperatingPeriodRef
from netex.operational_context_ref import OperationalContextRef
from netex.operator_ref import OperatorRef
from netex.organisation_part_ref import OrganisationPartRef
from netex.organisation_ref import OrganisationRef
from netex.organisational_unit_ref import OrganisationalUnitRef
from netex.other_organisation_ref import OtherOrganisationRef
from netex.parent_common_section_ref import ParentCommonSectionRef
from netex.parent_section_ref import ParentSectionRef
from netex.parking_area_ref import ParkingAreaRef
from netex.parking_bay_condition_ref import ParkingBayConditionRef
from netex.parking_bay_ref import ParkingBayRef
from netex.parking_bay_status_ref import ParkingBayStatusRef
from netex.parking_capacity_ref import ParkingCapacityRef
from netex.parking_charge_band_ref import ParkingChargeBandRef
from netex.parking_entrance_for_vehicles_ref import ParkingEntranceForVehiclesRef
from netex.parking_entrance_ref import ParkingEntranceRef
from netex.parking_passenger_entrance_ref import ParkingPassengerEntranceRef
from netex.parking_point_ref import ParkingPointRef
from netex.parking_price_ref import ParkingPriceRef
from netex.parking_properties_ref import ParkingPropertiesRef
from netex.parking_ref import ParkingRef
from netex.parking_tariff_ref import ParkingTariffRef
from netex.passenger_capacity_ref import PassengerCapacityRef
from netex.passenger_carrying_requirement_ref import PassengerCarryingRequirementRef
from netex.passenger_seat_ref import PassengerSeatRef
from netex.passing_time_ref import PassingTimeRef
from netex.path_junction_ref import PathJunctionRef
from netex.path_link_ref import PathLinkRef
from netex.penalty_policy_ref import PenaltyPolicyRef
from netex.personal_mode_of_operation_ref import PersonalModeOfOperationRef
from netex.place_ref import PlaceRef
from netex.point_of_interest_classification_ref import PointOfInterestClassificationRef
from netex.point_of_interest_entrance_ref import PointOfInterestEntranceRef
from netex.point_of_interest_hierarchy_ref import PointOfInterestHierarchyRef
from netex.point_of_interest_ref import PointOfInterestRef
from netex.point_of_interest_space_ref import PointOfInterestSpaceRef
from netex.point_of_interest_vehicle_entrance_ref import PointOfInterestVehicleEntranceRef
from netex.point_projection import PointProjection
from netex.point_projection_ref import PointProjectionRef
from netex.point_ref import PointRef
from netex.pool_of_vehicles_ref import PoolOfVehiclesRef
from netex.postal_address_ref import PostalAddressRef
from netex.preassigned_fare_product_ref import PreassignedFareProductRef
from netex.price_group_ref import PriceGroupRef
from netex.price_unit_ref import PriceUnitRef
from netex.priceable_object_ref import PriceableObjectRef
from netex.pricing_parameter_set_ref import PricingParameterSetRef
from netex.pricing_rule_ref import PricingRuleRef
from netex.pricing_service_ref import PricingServiceRef
from netex.profile_parameter_ref import ProfileParameterRef
from netex.purchase_window_ref import PurchaseWindowRef
from netex.purpose_of_equipment_profile_ref import PurposeOfEquipmentProfileRef
from netex.purpose_of_grouping_ref import PurposeOfGroupingRef
from netex.purpose_of_journey_partition_ref import PurposeOfJourneyPartitionRef
from netex.quality_structure_factor_price_ref import QualityStructureFactorPriceRef
from netex.quality_structure_factor_ref import QualityStructureFactorRef
from netex.quay_ref import QuayRef
from netex.railway_link_ref import RailwayLinkRef
from netex.railway_point_ref import RailwayPointRef
from netex.refunding_ref import RefundingRef
from netex.relief_opportunity_ref import ReliefOpportunityRef
from netex.relief_point_ref import ReliefPointRef
from netex.rental_availability_ref import RentalAvailabilityRef
from netex.rental_option_ref import RentalOptionRef
from netex.rental_penalty_policy_ref import RentalPenaltyPolicyRef
from netex.repeated_trip_fare_request_ref import RepeatedTripFareRequestRef
from netex.replacing_ref import ReplacingRef
from netex.requested_travel_specification_ref import RequestedTravelSpecificationRef
from netex.reselling_ref import ResellingRef
from netex.reserving_ref import ReservingRef
from netex.residential_qualification_eligibility_ref import ResidentialQualificationEligibilityRef
from netex.residential_qualification_ref import ResidentialQualificationRef
from netex.resource_frame_ref import ResourceFrameRef
from netex.responsibility_role_ref import ResponsibilityRoleRef
from netex.responsibility_set_ref import ResponsibilitySetRef
from netex.retail_consortium_ref import RetailConsortiumRef
from netex.retail_device_security_listing_ref import RetailDeviceSecurityListingRef
from netex.rhythmical_journey_group_ref import RhythmicalJourneyGroupRef
from netex.road_address_ref import RoadAddressRef
from netex.road_link_ref import RoadLinkRef
from netex.road_point_ref import RoadPointRef
from netex.round_trip_ref import RoundTripRef
from netex.rounding_ref import RoundingRef
from netex.rounding_step_ref import RoundingStepRef
from netex.route_instruction_ref import RouteInstructionRef
from netex.route_link_ref import RouteLinkRef
from netex.route_point_ref import RoutePointRef
from netex.route_ref import RouteRef
from netex.routing_constraint_zone_ref import RoutingConstraintZoneRef
from netex.routing_ref import RoutingRef
from netex.sale_discount_right_ref import SaleDiscountRightRef
from netex.sales_offer_package_element_ref import SalesOfferPackageElementRef
from netex.sales_offer_package_entitlement_given_ref import SalesOfferPackageEntitlementGivenRef
from netex.sales_offer_package_entitlement_required_ref import SalesOfferPackageEntitlementRequiredRef
from netex.sales_offer_package_price_ref import SalesOfferPackagePriceRef
from netex.sales_offer_package_ref import SalesOfferPackageRef
from netex.sales_transaction_frame_ref import SalesTransactionFrameRef
from netex.sales_transaction_ref import SalesTransactionRef
from netex.schedule_request_ref import ScheduleRequestRef
from netex.scheduled_mode_of_operation_ref import ScheduledModeOfOperationRef
from netex.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.schematic_map_member_ref import SchematicMapMemberRef
from netex.schematic_map_ref import SchematicMapRef
from netex.section_ref import SectionRef
from netex.series_constraint_price_ref import SeriesConstraintPriceRef
from netex.series_constraint_ref import SeriesConstraintRef
from netex.service_access_code_ref import ServiceAccessCodeRef
from netex.service_access_right_ref import ServiceAccessRightRef
from netex.service_calendar_frame_ref import ServiceCalendarFrameRef
from netex.service_calendar_ref import ServiceCalendarRef
from netex.service_facility_set_ref import ServiceFacilitySetRef
from netex.service_frame_ref import ServiceFrameRef
from netex.service_journey_interchange_ref import ServiceJourneyInterchangeRef
from netex.service_journey_pattern_interchange_ref import ServiceJourneyPatternInterchangeRef
from netex.service_journey_pattern_ref import ServiceJourneyPatternRef
from netex.service_journey_ref import ServiceJourneyRef
from netex.service_link_ref import ServiceLinkRef
from netex.service_pattern_ref import ServicePatternRef
from netex.service_site_ref import ServiceSiteRef
from netex.serviced_organisation_ref import ServicedOrganisationRef
from netex.simple_vehicle_type_ref import SimpleVehicleTypeRef
from netex.single_journey_path_ref import SingleJourneyPathRef
from netex.single_journey_ref import SingleJourneyRef
from netex.single_trip_fare_request_ref import SingleTripFareRequestRef
from netex.site_component_ref import SiteComponentRef
from netex.site_connection_ref import SiteConnectionRef
from netex.site_element_ref import SiteElementRef
from netex.site_facility_set_ref import SiteFacilitySetRef
from netex.site_frame_ref import SiteFrameRef
from netex.site_ref import SiteRef
from netex.smartcard_ref import SmartcardRef
from netex.special_service_ref import SpecialServiceRef
from netex.standard_fare_table_ref import StandardFareTableRef
from netex.start_time_at_stop_point_ref import StartTimeAtStopPointRef
from netex.step_limit_ref import StepLimitRef
from netex.stop_area_ref import StopAreaRef
from netex.stop_event_request_ref import StopEventRequestRef
from netex.stop_finder_request_ref import StopFinderRequestRef
from netex.stop_place_entrance_ref import StopPlaceEntranceRef
from netex.stop_place_ref import StopPlaceRef
from netex.stop_place_space_ref import StopPlaceSpaceRef
from netex.stop_place_vehicle_entrance_ref import StopPlaceVehicleEntranceRef
from netex.submode_ref import SubmodeRef
from netex.subscribing_ref import SubscribingRef
from netex.supplement_product_ref import SupplementProductRef
from netex.supply_contract_ref import SupplyContractRef
from netex.suspending_ref import SuspendingRef
from netex.target_passing_time_ref import TargetPassingTimeRef
from netex.tariff_object_ref import TariffObjectRef
from netex.tariff_ref import TariffRef
from netex.tariff_zone_ref import TariffZoneRef
from netex.taxi_parking_area_ref import TaxiParkingAreaRef
from netex.taxi_rank_ref import TaxiRankRef
from netex.taxi_stand_ref import TaxiStandRef
from netex.template_service_journey_ref import TemplateServiceJourneyRef
from netex.third_party_product_ref import ThirdPartyProductRef
from netex.time_demand_profile_ref import TimeDemandProfileRef
from netex.time_demand_type_ref import TimeDemandTypeRef
from netex.time_interval_price_ref import TimeIntervalPriceRef
from netex.time_interval_ref import TimeIntervalRef
from netex.time_structure_factor_ref import TimeStructureFactorRef
from netex.time_unit_price_ref import TimeUnitPriceRef
from netex.time_unit_ref import TimeUnitRef
from netex.timeband_ref import TimebandRef
from netex.timetable_frame_ref import TimetableFrameRef
from netex.timetabled_passing_time_ref import TimetabledPassingTimeRef
from netex.timing_algorithm_type_ref import TimingAlgorithmTypeRef
from netex.timing_link_ref import TimingLinkRef
from netex.timing_pattern_ref import TimingPatternRef
from netex.timing_point_ref import TimingPointRef
from netex.topographic_place_ref import TopographicPlaceRef
from netex.topographic_projection import TopographicProjection
from netex.topographic_projection_ref import TopographicProjectionRef
from netex.traffic_control_point_ref import TrafficControlPointRef
from netex.train_block_part_ref import TrainBlockPartRef
from netex.train_block_ref import TrainBlockRef
from netex.train_component_ref import TrainComponentRef
from netex.train_element_ref import TrainElementRef
from netex.train_in_compound_train_ref import TrainInCompoundTrainRef
from netex.train_number_ref import TrainNumberRef
from netex.train_ref import TrainRef
from netex.transferability_ref import TransferabilityRef
from netex.transport_administrative_zone_ref import TransportAdministrativeZoneRef
from netex.transport_type_ref import TransportTypeRef
from netex.travel_agent_ref import TravelAgentRef
from netex.travel_document_ref import TravelDocumentRef
from netex.travel_document_security_listing_ref import TravelDocumentSecurityListingRef
from netex.travel_specification_ref import TravelSpecificationRef
from netex.trip_leg_ref import TripLegRef
from netex.trip_pattern_trip_ref import TripPatternTripRef
from netex.trip_plan_request_ref import TripPlanRequestRef
from netex.trip_ref import TripRef
from netex.turnaround_time_limit_time_ref import TurnaroundTimeLimitTimeRef
from netex.type_of_access_right_assignment_ref import TypeOfAccessRightAssignmentRef
from netex.type_of_activation_ref import TypeOfActivationRef
from netex.type_of_battery_chemistry_ref import TypeOfBatteryChemistryRef
from netex.type_of_codespace_assignment_ref import TypeOfCodespaceAssignmentRef
from netex.type_of_concession_ref import TypeOfConcessionRef
from netex.type_of_congestion_ref import TypeOfCongestionRef
from netex.type_of_customer_account_ref import TypeOfCustomerAccountRef
from netex.type_of_delivery_variant_ref import TypeOfDeliveryVariantRef
from netex.type_of_equipment_ref import TypeOfEquipmentRef
from netex.type_of_facility_ref import TypeOfFacilityRef
from netex.type_of_fare_contract_entry_ref import TypeOfFareContractEntryRef
from netex.type_of_fare_contract_ref import TypeOfFareContractRef
from netex.type_of_fare_product_ref import TypeOfFareProductRef
from netex.type_of_fare_structure_element_ref import TypeOfFareStructureElementRef
from netex.type_of_fare_structure_factor_ref import TypeOfFareStructureFactorRef
from netex.type_of_fare_table_ref import TypeOfFareTableRef
from netex.type_of_feature_ref import TypeOfFeatureRef
from netex.type_of_fleet_ref import TypeOfFleetRef
from netex.type_of_flexible_service_ref import TypeOfFlexibleServiceRef
from netex.type_of_frame_ref import TypeOfFrameRef
from netex.type_of_journey_pattern_ref import TypeOfJourneyPatternRef
from netex.type_of_line_ref import TypeOfLineRef
from netex.type_of_link_ref import TypeOfLinkRef
from netex.type_of_link_sequence_ref import TypeOfLinkSequenceRef
from netex.type_of_machine_readability_ref import TypeOfMachineReadabilityRef
from netex.type_of_medium_access_device_ref import TypeOfMediumAccessDeviceRef
from netex.type_of_mobility_service_ref import TypeOfMobilityServiceRef
from netex.type_of_mode_of_operation_ref import TypeOfModeOfOperationRef
from netex.type_of_notice_ref import TypeOfNoticeRef
from netex.type_of_operation_ref import TypeOfOperationRef
from netex.type_of_organisation_part_ref import TypeOfOrganisationPartRef
from netex.type_of_organisation_ref import TypeOfOrganisationRef
from netex.type_of_parking_ref import TypeOfParkingRef
from netex.type_of_passenger_information_equipment_ref import TypeOfPassengerInformationEquipmentRef
from netex.type_of_payment_method_ref import TypeOfPaymentMethodRef
from netex.type_of_place_ref import TypeOfPlaceRef
from netex.type_of_plug_ref import TypeOfPlugRef
from netex.type_of_point_ref import TypeOfPointRef
from netex.type_of_pricing_rule_ref import TypeOfPricingRuleRef
from netex.type_of_product_category_ref import TypeOfProductCategoryRef
from netex.type_of_projection_ref import TypeOfProjectionRef
from netex.type_of_proof_ref import TypeOfProofRef
from netex.type_of_responsibility_role_ref import TypeOfResponsibilityRoleRef
from netex.type_of_retail_device_ref import TypeOfRetailDeviceRef
from netex.type_of_sales_offer_package_ref import TypeOfSalesOfferPackageRef
from netex.type_of_security_list_ref import TypeOfSecurityListRef
from netex.type_of_service_feature_ref import TypeOfServiceFeatureRef
from netex.type_of_service_ref import TypeOfServiceRef
from netex.type_of_tariff_ref import TypeOfTariffRef
from netex.type_of_time_demand_type_ref import TypeOfTimeDemandTypeRef
from netex.type_of_transfer_ref import TypeOfTransferRef
from netex.type_of_travel_document_ref import TypeOfTravelDocumentRef
from netex.type_of_usage_parameter_ref import TypeOfUsageParameterRef
from netex.type_of_validity_ref import TypeOfValidityRef
from netex.type_of_zone_ref import TypeOfZoneRef
from netex.uic_operating_period_ref import UicOperatingPeriodRef
from netex.usage_discount_right_ref import UsageDiscountRightRef
from netex.usage_parameter_price_ref import UsageParameterPriceRef
from netex.usage_validity_period_ref import UsageValidityPeriodRef
from netex.user_profile_eligibility_ref import UserProfileEligibilityRef
from netex.user_profile_ref import UserProfileRef
from netex.validable_element_price_ref import ValidableElementPriceRef
from netex.validable_element_ref import ValidableElementRef
from netex.validity_condition_ref import ValidityConditionRef
from netex.validity_rule_parameter_ref import ValidityRuleParameterRef
from netex.validity_trigger_ref import ValidityTriggerRef
from netex.vehicle_entrance_ref import VehicleEntranceRef
from netex.vehicle_equipment_profile_ref import VehicleEquipmentProfileRef
from netex.vehicle_journey_ref import VehicleJourneyRef
from netex.vehicle_manoeuvring_requirement_ref import VehicleManoeuvringRequirementRef
from netex.vehicle_meeting_link_ref import VehicleMeetingLinkRef
from netex.vehicle_meeting_place_ref import VehicleMeetingPlaceRef
from netex.vehicle_meeting_point_ref import VehicleMeetingPointRef
from netex.vehicle_model_ref import VehicleModelRef
from netex.vehicle_pooler_profile_ref import VehiclePoolerProfileRef
from netex.vehicle_pooling_driver_info_ref import VehiclePoolingDriverInfoRef
from netex.vehicle_pooling_meeting_place_ref import VehiclePoolingMeetingPlaceRef
from netex.vehicle_pooling_parking_area_ref import VehiclePoolingParkingAreaRef
from netex.vehicle_pooling_parking_bay_ref import VehiclePoolingParkingBayRef
from netex.vehicle_pooling_ref import VehiclePoolingRef
from netex.vehicle_position_alignment_ref import VehiclePositionAlignmentRef
from netex.vehicle_profile_ref import VehicleProfileRef
from netex.vehicle_quay_alignment_ref import VehicleQuayAlignmentRef
from netex.vehicle_ref import VehicleRef
from netex.vehicle_rental_ref import VehicleRentalRef
from netex.vehicle_requirement_ref import VehicleRequirementRef
from netex.vehicle_schedule_frame_ref import VehicleScheduleFrameRef
from netex.vehicle_service_part_ref import VehicleServicePartRef
from netex.vehicle_service_ref import VehicleServiceRef
from netex.vehicle_sharing_parking_area_ref import VehicleSharingParkingAreaRef
from netex.vehicle_sharing_parking_bay_ref import VehicleSharingParkingBayRef
from netex.vehicle_sharing_ref import VehicleSharingRef
from netex.vehicle_stopping_place_ref import VehicleStoppingPlaceRef
from netex.vehicle_stopping_position_ref import VehicleStoppingPositionRef
from netex.vehicle_type_preference_ref import VehicleTypePreferenceRef
from netex.vehicle_type_ref import VehicleTypeRef
from netex.vehicle_type_zone_restriction_ref import VehicleTypeZoneRestrictionRef
from netex.version_of_object_ref import VersionOfObjectRef
from netex.version_ref import VersionRef
from netex.whitelist_ref import WhitelistRef
from netex.wire_link_ref import WireLinkRef
from netex.wire_point_ref import WirePointRef
from netex.zone_projection import ZoneProjection
from netex.zone_projection_ref import ZoneProjectionRef
from netex.zone_ref import ZoneRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SchematicMapMemberVersionedChildStructure(VersionedChildStructure):
    """
    Type for a SCHEMATIC MAP MEMBER.

    :ivar name: Name of Element.
    :ivar choice:
    :ivar hide: Whether element is to be hidden on map.
    :ivar display_as_icon: Whether element is to be displayed on map as
        an icon.
    :ivar info_link:
    :ivar x: X pixel coordinate of member on map image  from origin at
        Bottom Left.
    :ivar y: Y pixel coordinate from origin at Bottom Left.
    :ivar choice_1:
    """
    class Meta:
        name = "SchematicMapMember_VersionedChildStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
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
                    "name": "PassingTimeRef",
                    "type": PassingTimeRef,
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
                    "name": "SupplyContractRef",
                    "type": SupplyContractRef,
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
                    "name": "MediumAccessDeviceSecurityListingRef",
                    "type": MediumAccessDeviceSecurityListingRef,
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
                    "name": "VehicleProfileRef",
                    "type": VehicleProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChargingEquipmentProfileRef",
                    "type": ChargingEquipmentProfileRef,
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
                    "name": "VehicleRef",
                    "type": VehicleRef,
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
                    "name": "NavigationPathRef",
                    "type": NavigationPathRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RouteRef",
                    "type": RouteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LinkSequenceRef",
                    "type": LinkSequenceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ContactRef",
                    "type": ContactRef,
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
                    "name": "AlternativeNameRef",
                    "type": AlternativeNameRef,
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
                    "name": "PathJunctionRef",
                    "type": PathJunctionRef,
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
                    "name": "PathLinkRef",
                    "type": PathLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RouteLinkRef",
                    "type": RouteLinkRef,
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
                    "name": "ResponsibilityRoleRef",
                    "type": ResponsibilityRoleRef,
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
                    "name": "GroupOfStopPlacesRef",
                    "type": GroupOfStopPlacesRef,
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
                    "name": "GroupOfOperatorsRef",
                    "type": GroupOfOperatorsRef,
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
                    "name": "DirectionRef",
                    "type": DirectionRef,
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
                    "name": "TypeOfZoneRef",
                    "type": TypeOfZoneRef,
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
        }
    )
    hide: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Hide",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    display_as_icon: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DisplayAsIcon",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    info_link: Optional[InfoLink] = field(
        default=None,
        metadata={
            "name": "InfoLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    x: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    y: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    choice_1: Optional[object] = field(
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
        }
    )
