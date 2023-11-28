from dataclasses import dataclass, field
from typing import List, Optional, Type
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlDuration
from netex.access_vehicle_equipment_ref import AccessVehicleEquipmentRef
from netex.activated_equipment_ref import ActivatedEquipmentRef
from netex.additional_driver_option_ref import AdditionalDriverOptionRef
from netex.alternative_names_rel_structure import AlternativeNamesRelStructure
from netex.alternative_texts_rel_structure import (
    DataManagedObjectStructure,
    VersionedChildStructure,
)
from netex.amount_of_price_unit_product_ref import AmountOfPriceUnitProductRef
from netex.assistance_booking_service_ref import AssistanceBookingServiceRef
from netex.assistance_service_ref import AssistanceServiceRef
from netex.authority_ref import AuthorityRef
from netex.battery_equipment_ref import BatteryEquipmentRef
from netex.booking_policy_ref import BookingPolicyRef
from netex.cancelling_ref import CancellingRef
from netex.capped_discount_right_ref import CappedDiscountRightRef
from netex.capping_rule_price import CappingRulePrice
from netex.capping_rule_price_ref import CappingRulePriceRef
from netex.capping_rule_ref import CappingRuleRef
from netex.car_model_profile_ref import CarModelProfileRef
from netex.car_pooling_service_ref import CarPoolingServiceRef
from netex.catering_service_ref import CateringServiceRef
from netex.cell_ref import CellRef
from netex.charging_policy_ref import ChargingPolicyRef
from netex.chauffeured_vehicle_service_ref import ChauffeuredVehicleServiceRef
from netex.class_of_use_ref import ClassOfUseRef
from netex.commercial_profile_ref import CommercialProfileRef
from netex.communication_service_ref import CommunicationServiceRef
from netex.companion_profile_ref import CompanionProfileRef
from netex.complaints_service_ref import ComplaintsServiceRef
from netex.compound_train_ref import CompoundTrainRef
from netex.controllable_element_price import ControllableElementPrice
from netex.controllable_element_price_ref import ControllableElementPriceRef
from netex.controllable_element_ref import ControllableElementRef
from netex.crossing_equipment_ref import CrossingEquipmentRef
from netex.customer_purchase_package_element_ref import CustomerPurchasePackageElementRef
from netex.customer_purchase_package_price import CustomerPurchasePackagePrice
from netex.customer_purchase_package_price_ref import CustomerPurchasePackagePriceRef
from netex.customer_purchase_package_ref import CustomerPurchasePackageRef
from netex.customer_service_ref import CustomerServiceRef
from netex.cycle_model_profile_ref import CycleModelProfileRef
from netex.cycle_storage_equipment_ref import CycleStorageEquipmentRef
from netex.discounting_rule_ref import DiscountingRuleRef
from netex.distance_matrix_element_inverse_ref import DistanceMatrixElementInverseRef
from netex.distance_matrix_element_price import DistanceMatrixElementPrice
from netex.distance_matrix_element_price_ref import DistanceMatrixElementPriceRef
from netex.distance_matrix_element_ref import DistanceMatrixElementRef
from netex.distribution_channel_ref import DistributionChannelRef
from netex.eligibility_change_policy_ref import EligibilityChangePolicyRef
from netex.entitlement_given_ref import EntitlementGivenRef
from netex.entitlement_product_ref import EntitlementProductRef
from netex.entitlement_required_ref import EntitlementRequiredRef
from netex.entrance_equipment_ref import EntranceEquipmentRef
from netex.equipment_ref import EquipmentRef
from netex.escalator_equipment_ref import EscalatorEquipmentRef
from netex.exchanging_ref import ExchangingRef
from netex.facility_set_ref import FacilitySetRef
from netex.fare_class_enumeration import FareClassEnumeration
from netex.fare_demand_factor_ref import FareDemandFactorRef
from netex.fare_price_ref import FarePriceRef
from netex.fare_price_versioned_child_structure import FarePriceVersionedChildStructure
from netex.fare_product_price import FareProductPrice
from netex.fare_product_price_ref import FareProductPriceRef
from netex.fare_product_ref import FareProductRef
from netex.fare_quota_factor_ref import FareQuotaFactorRef
from netex.fare_section_ref import FareSectionRef
from netex.fare_structure_element_price import FareStructureElementPrice
from netex.fare_structure_element_price_ref import FareStructureElementPriceRef
from netex.fare_structure_element_ref import FareStructureElementRef
from netex.fare_table_column_ref_structure import FareTableColumnRefStructure
from netex.fare_table_column_versioned_child_structure import FareTableColumnsRelStructure
from netex.fare_table_ref import FareTableRef
from netex.fare_table_row_ref_structure import FareTableRowRefStructure
from netex.fare_table_row_versioned_child_structure import FareTableRowsRelStructure
from netex.fare_table_specifics_structure import FareTableSpecificsStructure
from netex.flexible_line_ref import FlexibleLineRef
from netex.frequency_of_use_ref import FrequencyOfUseRef
from netex.fulfilment_method_price import FulfilmentMethodPrice
from netex.fulfilment_method_price_ref import FulfilmentMethodPriceRef
from netex.fulfilment_method_ref import FulfilmentMethodRef
from netex.general_organisation_ref import GeneralOrganisationRef
from netex.general_sign_ref import GeneralSignRef
from netex.geographical_interval_price import GeographicalIntervalPrice
from netex.geographical_interval_price_ref import GeographicalIntervalPriceRef
from netex.geographical_interval_ref import GeographicalIntervalRef
from netex.geographical_structure_factor_ref import GeographicalStructureFactorRef
from netex.geographical_unit_price import GeographicalUnitPrice
from netex.geographical_unit_price_ref import GeographicalUnitPriceRef
from netex.group_of_distance_matrix_elements_ref import GroupOfDistanceMatrixElementsRef
from netex.group_of_distribution_channels_ref import GroupOfDistributionChannelsRef
from netex.group_of_entities_version_structure import GroupOfEntitiesVersionStructure
from netex.group_of_lines_ref import GroupOfLinesRef
from netex.group_of_services_ref import GroupOfServicesRef
from netex.group_of_single_journeys_ref import GroupOfSingleJourneysRef
from netex.group_ticket_ref import GroupTicketRef
from netex.heading_sign_ref import HeadingSignRef
from netex.help_point_equipment_ref import HelpPointEquipmentRef
from netex.hire_service_ref import HireServiceRef
from netex.info_links_rel_structure import InfoLinksRelStructure
from netex.interchanging_ref import InterchangingRef
from netex.left_luggage_service_ref import LeftLuggageServiceRef
from netex.lift_equipment_ref import LiftEquipmentRef
from netex.limiting_rule_ref import LimitingRuleRef
from netex.line_ref import LineRef
from netex.local_service_ref import LocalServiceRef
from netex.lost_property_service_ref import LostPropertyServiceRef
from netex.luggage_allowance_ref import LuggageAllowanceRef
from netex.luggage_locker_equipment_ref import LuggageLockerEquipmentRef
from netex.luggage_service_ref import LuggageServiceRef
from netex.management_agent_ref import ManagementAgentRef
from netex.meeting_point_service_ref import MeetingPointServiceRef
from netex.minimum_stay_ref import MinimumStayRef
from netex.money_service_ref import MoneyServiceRef
from netex.multilingual_string import MultilingualString
from netex.network_ref import NetworkRef
from netex.notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from netex.online_service_operator_ref import OnlineServiceOperatorRef
from netex.online_service_ref import OnlineServiceRef
from netex.operator_ref import OperatorRef
from netex.organisation_ref import OrganisationRef
from netex.other_organisation_ref import OtherOrganisationRef
from netex.parking_charge_band_ref import ParkingChargeBandRef
from netex.parking_price_ref import ParkingPriceRef
from netex.parking_properties_ref import ParkingPropertiesRef
from netex.parking_ref import ParkingRef
from netex.parking_tariff_ref import ParkingTariffRef
from netex.parking_vehicle_enumeration import ParkingVehicleEnumeration
from netex.passenger_equipment_ref import PassengerEquipmentRef
from netex.passenger_information_equipment_ref import PassengerInformationEquipmentRef
from netex.passenger_safety_equipment_ref import PassengerSafetyEquipmentRef
from netex.payment_method_enumeration import PaymentMethodEnumeration
from netex.penalty_policy_ref import PenaltyPolicyRef
from netex.place_lighting_equipment_ref import PlaceLightingEquipmentRef
from netex.place_sign_ref import PlaceSignRef
from netex.point_of_interest_ref import PointOfInterestRef
from netex.preassigned_fare_product_ref import PreassignedFareProductRef
from netex.price_group_ref import PriceGroupRef
from netex.priceable_object_ref import PriceableObjectRef
from netex.priceable_object_refs_rel_structure import PriceableObjectRefsRelStructure
from netex.pricing_rule_ref import PricingRuleRef
from netex.pricing_service_ref import PricingServiceRef
from netex.private_code import PrivateCode
from netex.profile_parameter_ref import ProfileParameterRef
from netex.purchase_window_ref import PurchaseWindowRef
from netex.quality_structure_factor_price import QualityStructureFactorPrice
from netex.quality_structure_factor_price_ref import QualityStructureFactorPriceRef
from netex.quality_structure_factor_ref import QualityStructureFactorRef
from netex.queueing_equipment_ref import QueueingEquipmentRef
from netex.ramp_equipment_ref import RampEquipmentRef
from netex.refuelling_equipment_ref import RefuellingEquipmentRef
from netex.refunding_ref import RefundingRef
from netex.relative_direction_enumeration import RelativeDirectionEnumeration
from netex.rental_option_ref import RentalOptionRef
from netex.rental_penalty_policy_ref import RentalPenaltyPolicyRef
from netex.replacing_ref import ReplacingRef
from netex.reselling_ref import ResellingRef
from netex.reserving_ref import ReservingRef
from netex.retail_consortium_ref import RetailConsortiumRef
from netex.retail_device_ref import RetailDeviceRef
from netex.retail_service_ref import RetailServiceRef
from netex.rough_surface_ref import RoughSurfaceRef
from netex.round_trip_ref import RoundTripRef
from netex.rounding_ref import RoundingRef
from netex.routing_ref import RoutingRef
from netex.routing_type_enumeration import RoutingTypeEnumeration
from netex.rubbish_disposal_equipment_ref import RubbishDisposalEquipmentRef
from netex.sale_discount_right_ref import SaleDiscountRightRef
from netex.sales_offer_package_element_ref import SalesOfferPackageElementRef
from netex.sales_offer_package_entitlement_given_ref import SalesOfferPackageEntitlementGivenRef
from netex.sales_offer_package_entitlement_required_ref import SalesOfferPackageEntitlementRequiredRef
from netex.sales_offer_package_price import SalesOfferPackagePrice
from netex.sales_offer_package_price_ref import SalesOfferPackagePriceRef
from netex.sales_offer_package_ref import SalesOfferPackageRef
from netex.sanitary_equipment_ref import SanitaryEquipmentRef
from netex.seating_equipment_ref import SeatingEquipmentRef
from netex.series_constraint_price import SeriesConstraintPrice
from netex.series_constraint_price_ref import SeriesConstraintPriceRef
from netex.series_constraint_ref import SeriesConstraintRef
from netex.service_access_right_ref import ServiceAccessRightRef
from netex.service_facility_set_ref import ServiceFacilitySetRef
from netex.service_journey_ref import ServiceJourneyRef
from netex.service_site_ref import ServiceSiteRef
from netex.serviced_organisation_ref import ServicedOrganisationRef
from netex.shelter_equipment_ref import ShelterEquipmentRef
from netex.sign_equipment_ref import SignEquipmentRef
from netex.simple_vehicle_type_ref import SimpleVehicleTypeRef
from netex.single_journey_ref import SingleJourneyRef
from netex.site_equipment_ref import SiteEquipmentRef
from netex.site_facility_set_ref import SiteFacilitySetRef
from netex.site_ref import SiteRef
from netex.staircase_equipment_ref import StaircaseEquipmentRef
from netex.standard_fare_table import StandardFareTable
from netex.standard_fare_table_ref import StandardFareTableRef
from netex.step_limit_ref import StepLimitRef
from netex.stop_place_ref import StopPlaceRef
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from netex.subscribing_ref import SubscribingRef
from netex.supplement_product_ref import SupplementProductRef
from netex.suspending_ref import SuspendingRef
from netex.tariff_ref import TariffRef
from netex.tariff_zone_ref import TariffZoneRef
from netex.taxi_rank_ref import TaxiRankRef
from netex.taxi_service_ref import TaxiServiceRef
from netex.template_service_journey_ref import TemplateServiceJourneyRef
from netex.third_party_product_ref import ThirdPartyProductRef
from netex.ticket_validator_equipment_ref import TicketValidatorEquipmentRef
from netex.ticketing_equipment_ref import TicketingEquipmentRef
from netex.ticketing_service_ref import TicketingServiceRef
from netex.time_interval_price import TimeIntervalPrice
from netex.time_interval_price_ref import TimeIntervalPriceRef
from netex.time_interval_ref import TimeIntervalRef
from netex.time_structure_factor_ref import TimeStructureFactorRef
from netex.time_unit_price import TimeUnitPrice
from netex.time_unit_price_ref import TimeUnitPriceRef
from netex.time_unit_ref import TimeUnitRef
from netex.train_number_ref import TrainNumberRef
from netex.train_ref import TrainRef
from netex.transferability_ref import TransferabilityRef
from netex.transport_type_ref import TransportTypeRef
from netex.travel_agent_ref import TravelAgentRef
from netex.travelator_equipment_ref import TravelatorEquipmentRef
from netex.trolley_stand_equipment_ref import TrolleyStandEquipmentRef
from netex.type_of_fare_product_ref import TypeOfFareProductRef
from netex.type_of_fare_structure_factor_ref import TypeOfFareStructureFactorRef
from netex.type_of_fare_table_ref import TypeOfFareTableRef
from netex.type_of_parking_ref import TypeOfParkingRef
from netex.type_of_payment_method_ref import TypeOfPaymentMethodRef
from netex.type_of_product_category_ref import TypeOfProductCategoryRef
from netex.type_of_service_ref import TypeOfServiceRef
from netex.type_of_travel_document_ref import TypeOfTravelDocumentRef
from netex.usage_discount_right_ref import UsageDiscountRightRef
from netex.usage_parameter_price import UsageParameterPrice
from netex.usage_parameter_price_ref import UsageParameterPriceRef
from netex.usage_parameter_refs_rel_structure import UsageParameterRefsRelStructure
from netex.usage_validity_period_ref import UsageValidityPeriodRef
from netex.used_in_refs_rel_structure import UsedInRefsRelStructure
from netex.user_profile_ref import UserProfileRef
from netex.validable_element_price import ValidableElementPrice
from netex.validable_element_price_ref import ValidableElementPriceRef
from netex.validable_element_ref import ValidableElementRef
from netex.vehicle_charging_equipment_ref import VehicleChargingEquipmentRef
from netex.vehicle_equipment_ref import VehicleEquipmentRef
from netex.vehicle_meeting_place_ref import VehicleMeetingPlaceRef
from netex.vehicle_model_ref import VehicleModelRef
from netex.vehicle_pooler_profile_ref import VehiclePoolerProfileRef
from netex.vehicle_pooling_meeting_place_ref import VehiclePoolingMeetingPlaceRef
from netex.vehicle_release_equipment_ref import VehicleReleaseEquipmentRef
from netex.vehicle_rental_service_ref import VehicleRentalServiceRef
from netex.vehicle_sharing_service_ref import VehicleSharingServiceRef
from netex.vehicle_type_ref import VehicleTypeRef
from netex.waiting_equipment_ref import WaitingEquipmentRef
from netex.waiting_room_equipment_ref import WaitingRoomEquipmentRef
from netex.wheelchair_vehicle_ref import WheelchairVehicleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CellVersionedChildStructure(VersionedChildStructure):
    """
    Type for a CELL.

    :ivar name: Name of CELL.
    :ivar description: Description of CELL.
    :ivar choice:
    :ivar choice_1:
    :ivar group_of_distance_matrix_elements_ref:
    :ivar direction_type: For fares for DISTANCE MATRIXE LEMENTs,
        DIRECTION in which price applies.
    :ivar routing_type: Whether fare is for s a direct i.e. no changes
        required point to point  fare or indirect routing.
    :ivar authority_ref_or_operator_ref:
    :ivar network_ref_or_group_of_lines_ref:
    :ivar flexible_line_ref_or_line_ref:
    :ivar choice_2:
    :ivar
        vehicle_pooling_meeting_place_ref_or_vehicle_meeting_place_ref:
    :ivar type_of_parking_ref:
    :ivar tariff_zone_ref:
    :ivar fare_section_ref:
    :ivar fare_class:
    :ivar class_of_use_ref:
    :ivar
        service_facility_set_ref_or_site_facility_set_ref_or_facility_set_ref:
    :ivar type_of_product_category_ref:
    :ivar type_of_service_ref:
    :ivar choice_3:
    :ivar choice_4:
    :ivar vehicle_model_ref:
    :ivar cycle_model_profile_ref_or_car_model_profile_ref:
    :ivar choice_5:
    :ivar type_of_fare_product_ref:
    :ivar
        distribution_channel_ref_or_group_of_distribution_channels_ref:
    :ivar payment_method: Preferred payment Method .
    :ivar type_of_payment_method_ref:
    :ivar type_of_travel_document_ref:
    :ivar standard_fare_table_ref_or_fare_table_ref:
    :ivar column_ref: Column for CELL.
    :ivar row_ref: Row for CELL.
    :ivar notice_assignments: NOTICE relating to CElll
    :ivar order: Order in which cell is to appear.
    """
    class Meta:
        name = "Cell_VersionedChildStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
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
                    "name": "CellPrice",
                    "type": FarePriceVersionedChildStructure,
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
                    "name": "CustomerPurchasePackagePrice",
                    "type": CustomerPurchasePackagePrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPrice",
                    "type": Type["ParkingPrice"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackagePrice",
                    "type": SalesOfferPackagePrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FulfilmentMethodPrice",
                    "type": FulfilmentMethodPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappingRulePrice",
                    "type": CappingRulePrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareProductPrice",
                    "type": FareProductPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElementPrice",
                    "type": FareStructureElementPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeIntervalPrice",
                    "type": TimeIntervalPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeUnitPrice",
                    "type": TimeUnitPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QualityStructureFactorPrice",
                    "type": QualityStructureFactorPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControllableElementPrice",
                    "type": ControllableElementPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidableElementPrice",
                    "type": ValidableElementPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageParameterPrice",
                    "type": UsageParameterPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElementPrice",
                    "type": DistanceMatrixElementPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalIntervalPrice",
                    "type": GeographicalIntervalPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalUnitPrice",
                    "type": GeographicalUnitPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeriesConstraintPrice",
                    "type": SeriesConstraintPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PriceGroupRef",
                    "type": PriceGroupRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    choice_1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
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
            ),
        }
    )
    group_of_distance_matrix_elements_ref: Optional[GroupOfDistanceMatrixElementsRef] = field(
        default=None,
        metadata={
            "name": "GroupOfDistanceMatrixElementsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    direction_type: Optional[RelativeDirectionEnumeration] = field(
        default=None,
        metadata={
            "name": "DirectionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    routing_type: Optional[RoutingTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "RoutingType",
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
    network_ref_or_group_of_lines_ref: Optional[object] = field(
        default=None,
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
        }
    )
    flexible_line_ref_or_line_ref: Optional[object] = field(
        default=None,
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
        }
    )
    choice_2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
            ),
        }
    )
    vehicle_pooling_meeting_place_ref_or_vehicle_meeting_place_ref: Optional[object] = field(
        default=None,
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
        }
    )
    type_of_parking_ref: Optional[TypeOfParkingRef] = field(
        default=None,
        metadata={
            "name": "TypeOfParkingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tariff_zone_ref: Optional[TariffZoneRef] = field(
        default=None,
        metadata={
            "name": "TariffZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_section_ref: Optional[FareSectionRef] = field(
        default=None,
        metadata={
            "name": "FareSectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_class: Optional[FareClassEnumeration] = field(
        default=None,
        metadata={
            "name": "FareClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    class_of_use_ref: Optional[ClassOfUseRef] = field(
        default=None,
        metadata={
            "name": "ClassOfUseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_facility_set_ref_or_site_facility_set_ref_or_facility_set_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
        }
    )
    type_of_product_category_ref: Optional[TypeOfProductCategoryRef] = field(
        default=None,
        metadata={
            "name": "TypeOfProductCategoryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_service_ref: Optional[TypeOfServiceRef] = field(
        default=None,
        metadata={
            "name": "TypeOfServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    choice_3: Optional[object] = field(
        default=None,
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
                {
                    "name": "SingleJourneyRef",
                    "type": SingleJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainNumberRef",
                    "type": TrainNumberRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfServicesRef",
                    "type": GroupOfServicesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfSingleJourneysRef",
                    "type": GroupOfSingleJourneysRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    choice_4: Optional[object] = field(
        default=None,
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
        }
    )
    vehicle_model_ref: Optional[VehicleModelRef] = field(
        default=None,
        metadata={
            "name": "VehicleModelRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    cycle_model_profile_ref_or_car_model_profile_ref: Optional[object] = field(
        default=None,
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
        }
    )
    choice_5: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RetailDeviceRef",
                    "type": RetailDeviceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                    "name": "ActivatedEquipmentRef",
                    "type": ActivatedEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BatteryEquipmentRef",
                    "type": BatteryEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RefuellingEquipmentRef",
                    "type": RefuellingEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleChargingEquipmentRef",
                    "type": VehicleChargingEquipmentRef,
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
                {
                    "name": "LocalServiceRef",
                    "type": LocalServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleReleaseEquipmentRef",
                    "type": VehicleReleaseEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TicketValidatorEquipmentRef",
                    "type": TicketValidatorEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TicketingEquipmentRef",
                    "type": TicketingEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerInformationEquipmentRef",
                    "type": PassengerInformationEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CycleStorageEquipmentRef",
                    "type": CycleStorageEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrolleyStandEquipmentRef",
                    "type": TrolleyStandEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeatingEquipmentRef",
                    "type": SeatingEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ShelterEquipmentRef",
                    "type": ShelterEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LuggageLockerEquipmentRef",
                    "type": LuggageLockerEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WaitingRoomEquipmentRef",
                    "type": WaitingRoomEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WaitingEquipmentRef",
                    "type": WaitingEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteEquipmentRef",
                    "type": SiteEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PlaceLightingEquipmentRef",
                    "type": PlaceLightingEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoughSurfaceRef",
                    "type": RoughSurfaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StaircaseEquipmentRef",
                    "type": StaircaseEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QueueingEquipmentRef",
                    "type": QueueingEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelatorEquipmentRef",
                    "type": TravelatorEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EscalatorEquipmentRef",
                    "type": EscalatorEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LiftEquipmentRef",
                    "type": LiftEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CrossingEquipmentRef",
                    "type": CrossingEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RampEquipmentRef",
                    "type": RampEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntranceEquipmentRef",
                    "type": EntranceEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HeadingSignRef",
                    "type": HeadingSignRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralSignRef",
                    "type": GeneralSignRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PlaceSignRef",
                    "type": PlaceSignRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SignEquipmentRef",
                    "type": SignEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RubbishDisposalEquipmentRef",
                    "type": RubbishDisposalEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HelpPointEquipmentRef",
                    "type": HelpPointEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerSafetyEquipmentRef",
                    "type": PassengerSafetyEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SanitaryEquipmentRef",
                    "type": SanitaryEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WheelchairVehicleRef",
                    "type": WheelchairVehicleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessVehicleEquipmentRef",
                    "type": AccessVehicleEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleEquipmentRef",
                    "type": VehicleEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerEquipmentRef",
                    "type": PassengerEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EquipmentRef",
                    "type": EquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    type_of_fare_product_ref: Optional[TypeOfFareProductRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFareProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distribution_channel_ref_or_group_of_distribution_channels_ref: Optional[object] = field(
        default=None,
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
        }
    )
    payment_method: Optional[PaymentMethodEnumeration] = field(
        default=None,
        metadata={
            "name": "PaymentMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_payment_method_ref: Optional[TypeOfPaymentMethodRef] = field(
        default=None,
        metadata={
            "name": "TypeOfPaymentMethodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_travel_document_ref: Optional[TypeOfTravelDocumentRef] = field(
        default=None,
        metadata={
            "name": "TypeOfTravelDocumentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    standard_fare_table_ref_or_fare_table_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
            ),
        }
    )
    column_ref: Optional[FareTableColumnRefStructure] = field(
        default=None,
        metadata={
            "name": "ColumnRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    row_ref: Optional[FareTableRowRefStructure] = field(
        default=None,
        metadata={
            "name": "RowRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notice_assignments: Optional[NoticeAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingPriceVersionedChildStructure(FarePriceVersionedChildStructure):
    """
    Type for a PARKING TARIFF PRICEs.
    """
    class Meta:
        name = "ParkingPrice_VersionedChildStructure"

    parking_tariff_ref_or_parking_charge_band: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ParkingTariffRef",
                    "type": ParkingTariffRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingChargeBand",
                    "type": Type["ParkingChargeBand"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class Cell(CellVersionedChildStructure):
    """
    An individual combination of features in a FARE TABLE, used to associate a FARE
    PRICE.
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
class ParkingPrice(ParkingPriceVersionedChildStructure):
    """A set of all possible price features of a PARKING TARIFF ELEMENT: default total price, discount in value or percentage etc."""
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class CellsRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of FARE CELL.s.
    """
    class Meta:
        name = "cells_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Cell",
                    "type": Cell,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CellInContext",
                    "type": CellVersionedChildStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerPurchasePackagePrice",
                    "type": CustomerPurchasePackagePrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPrice",
                    "type": Type["ParkingPrice"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackagePrice",
                    "type": SalesOfferPackagePrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FulfilmentMethodPrice",
                    "type": FulfilmentMethodPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappingRulePrice",
                    "type": CappingRulePrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareProductPrice",
                    "type": FareProductPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElementPrice",
                    "type": FareStructureElementPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeIntervalPrice",
                    "type": TimeIntervalPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeUnitPrice",
                    "type": TimeUnitPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QualityStructureFactorPrice",
                    "type": QualityStructureFactorPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControllableElementPrice",
                    "type": ControllableElementPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidableElementPrice",
                    "type": ValidableElementPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageParameterPrice",
                    "type": UsageParameterPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElementPrice",
                    "type": DistanceMatrixElementPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalIntervalPrice",
                    "type": GeographicalIntervalPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalUnitPrice",
                    "type": GeographicalUnitPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeriesConstraintPrice",
                    "type": SeriesConstraintPrice,
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
                    "name": "CellRef",
                    "type": CellRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class FarePricesRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of FARE PRICEs.
    """
    class Meta:
        name = "farePrices_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
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
                    "name": "CellRef",
                    "type": CellRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerPurchasePackagePrice",
                    "type": CustomerPurchasePackagePrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPrice",
                    "type": ParkingPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackagePrice",
                    "type": SalesOfferPackagePrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FulfilmentMethodPrice",
                    "type": FulfilmentMethodPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappingRulePrice",
                    "type": CappingRulePrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareProductPrice",
                    "type": FareProductPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElementPrice",
                    "type": FareStructureElementPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeIntervalPrice",
                    "type": TimeIntervalPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeUnitPrice",
                    "type": TimeUnitPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QualityStructureFactorPrice",
                    "type": QualityStructureFactorPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControllableElementPrice",
                    "type": ControllableElementPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidableElementPrice",
                    "type": ValidableElementPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageParameterPrice",
                    "type": UsageParameterPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElementPrice",
                    "type": DistanceMatrixElementPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalIntervalPrice",
                    "type": GeographicalIntervalPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalUnitPrice",
                    "type": GeographicalUnitPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeriesConstraintPrice",
                    "type": SeriesConstraintPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class FareTableVersionStructure(GroupOfEntitiesVersionStructure):
    """
    Type for a FARE TABLE.

    :ivar start_date: Start date for PRICE GROUP.
    :ivar end_date: End date for PRICE GROUP.
    :ivar rounding_ref:
    :ivar type_of_fare_table_ref:
    :ivar prices_for: Combination of Elements for which this table
        provides PRICEs.
    :ivar used_in: Elements that use FARE TABLE that are not PRICEABLE
        OBJECTs.
    :ivar choice:
    :ivar limitations: Usage parameters common to all cells in table.
    :ivar specifics: Common factors shared with all cells.
    :ivar columns: Column headings to use when presenting table.
    :ivar rows: Row headings to use when presenting table.
    :ivar includes: Sub tables contained in table.
    :ivar embargo_until: Prices must not be released until this date.
    :ivar prices: Cells in the table.
    :ivar cells: Cells in the table.
    :ivar notice_assignments: NOTICEs that apply to whole FARE TABLE
    """
    class Meta:
        name = "FareTable_VersionStructure"

    start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    rounding_ref: Optional[RoundingRef] = field(
        default=None,
        metadata={
            "name": "RoundingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_fare_table_ref: Optional[TypeOfFareTableRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFareTableRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    prices_for: Optional[PriceableObjectRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "pricesFor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    used_in: Optional[UsedInRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "usedIn",
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
    limitations: Optional[UsageParameterRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    specifics: Optional[FareTableSpecificsStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    columns: Optional[FareTableColumnsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    rows: Optional[FareTableRowsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    includes: Optional["FareTablesRelStructure"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    embargo_until: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EmbargoUntil",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    prices: Optional["FarePricesRelStructure"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    cells: Optional[CellsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notice_assignments: Optional[NoticeAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class PriceGroupVersionStructure(GroupOfEntitiesVersionStructure):
    """
    Type for PRICE GROUP.

    :ivar start_date: Start date for PRICE GROUP.
    :ivar end_date: End date for PRICE GROUP.
    :ivar rounding_ref:
    :ivar members: PRICEs in PRICE GROUP.
    :ivar choice:
    """
    class Meta:
        name = "PriceGroup_VersionStructure"

    start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    rounding_ref: Optional[RoundingRef] = field(
        default=None,
        metadata={
            "name": "RoundingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    members: Optional[FarePricesRelStructure] = field(
        default=None,
        metadata={
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
            ),
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class FareTable(FareTableVersionStructure):
    """
    A grouping of prices that may be associated with a DISTANCE MATRIX ELEMENT,
    FARE STRUCTURE ELEMENT or  other PRICEABLE OBJECT.
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
class FareTableInContext(FareTableVersionStructure):
    """A grouping of prices that may be associated with a DISTANCE MATRIX ELEMENT,
    FARE STRUCTURE ELEMENT or  other PRICEABLE OBJECT.

    OPTIMIZATION - Alias for FARE TABLE That does not require an ID to be present.
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
class PriceGroup(PriceGroupVersionStructure):
    """
    A grouping of prices, allowing the grouping of numerous possible consumption
    elements into a limited number of price references, or to apply grouped
    increase, in value or percentage.
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
class FareTablesRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of FAREFARE TABLE PRICE GROUP.s.
    """
    class Meta:
        name = "fareTables_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
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
                    "name": "StandardFareTable",
                    "type": StandardFareTable,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareTableInContext",
                    "type": FareTableInContext,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareTable",
                    "type": FareTable,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class PriceGroupsRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of FARE PRICEs.
    """
    class Meta:
        name = "priceGroups_RelStructure"

    price_group_ref_or_price_group: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PriceGroupRef",
                    "type": PriceGroupRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PriceGroup",
                    "type": PriceGroup,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class PriceableObjectVersionStructure(DataManagedObjectStructure):
    """
    Type for PRICEABLE OBJECT.

    :ivar name: Name of PRICEABLE OBJECT.
    :ivar description: Description of PRICEABLE OBJECT.
    :ivar url: URL for information on element.
    :ivar info_links: Hyperlinks associated with GPRICEABLE OBLECT. Can
        be used to associated pfs, web pages etc, conditions of use etc.
    :ivar alternative_names: ALTERNATIVE NAMEs for PRICEABLE OBJECT.
    :ivar notice_assignments: NOTICE ASSIGNMENTs for PRICEABLE OBJECT.
    :ivar pricing_service_ref:
    :ivar limiting_rule_ref_or_discounting_rule_ref_or_pricing_rule_ref:
    :ivar price_groups: PRICE GROUPSs  making up FARE PRODUCT.
    :ivar fare_tables: Other FARE TABLESs for DISTANCE MATRIX ELEMENT.
    """
    class Meta:
        name = "PriceableObject_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "Url",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    info_links: Optional[InfoLinksRelStructure] = field(
        default=None,
        metadata={
            "name": "infoLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    alternative_names: Optional[AlternativeNamesRelStructure] = field(
        default=None,
        metadata={
            "name": "alternativeNames",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notice_assignments: Optional[NoticeAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    pricing_service_ref: Optional[PricingServiceRef] = field(
        default=None,
        metadata={
            "name": "PricingServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    limiting_rule_ref_or_discounting_rule_ref_or_pricing_rule_ref: Optional[object] = field(
        default=None,
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
        }
    )
    price_groups: Optional[PriceGroupsRelStructure] = field(
        default=None,
        metadata={
            "name": "priceGroups",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_tables: Optional[FareTablesRelStructure] = field(
        default=None,
        metadata={
            "name": "fareTables",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class FareStructureFactorVersionStructure(PriceableObjectVersionStructure):
    """
    Type for FARE STRUCTURE FACTOR.

    :ivar private_code:
    :ivar type_of_fare_structure_factor_ref:
    :ivar factor: Factor value assoictaed with init.
    """
    class Meta:
        name = "FareStructureFactor_VersionStructure"

    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_fare_structure_factor_ref: Optional[TypeOfFareStructureFactorRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFareStructureFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    factor: Optional[object] = field(
        default=None,
        metadata={
            "name": "Factor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class TimeStructureFactorVersionStructure(FareStructureFactorVersionStructure):
    """
    Type for TIME STRUCTURE FACTOR.
    """
    class Meta:
        name = "TimeStructureFactor_VersionStructure"

    parking_tariff_ref_or_tariff_ref: Optional[object] = field(
        default=None,
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
        }
    )
    time_interval_ref: Optional[TimeIntervalRef] = field(
        default=None,
        metadata={
            "name": "TimeIntervalRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_unit_ref: Optional[TimeUnitRef] = field(
        default=None,
        metadata={
            "name": "TimeUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_quota_factor_ref_or_fare_demand_factor_ref_or_quality_structure_factor_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
            ),
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingChargeBandVersionStructure(TimeStructureFactorVersionStructure):
    """
    Type for a PARKING TARIFF CHARGE BAND.

    :ivar parking_properties_ref:
    :ivar parking_vehicle_type: Type of vehicle for which this is the
        PARKING TARIFF CHARGE BAND.
    :ivar choice:
    :ivar maximum_stay: Maximum allowed stay duration for tariff amount.
    :ivar prices: Prices for PARKING TARIFF CHARGE BAND.
    """
    class Meta:
        name = "ParkingChargeBand_VersionStructure"

    parking_properties_ref: Optional[ParkingPropertiesRef] = field(
        default=None,
        metadata={
            "name": "ParkingPropertiesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_vehicle_type: Optional[ParkingVehicleEnumeration] = field(
        default=None,
        metadata={
            "name": "ParkingVehicleType",
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
            ),
        }
    )
    maximum_stay: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumStay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    prices: Optional["FarePricesRelStructure"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingChargeBand(ParkingChargeBandVersionStructure):
    """
    Parking charges that describe the cost of using a PARKING or PARKING AREA for a
    given period.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
