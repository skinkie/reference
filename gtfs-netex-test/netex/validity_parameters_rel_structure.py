from dataclasses import dataclass, field
from typing import List
from netex.access_space_ref import AccessSpaceRef
from netex.address_ref import AddressRef
from netex.all_authorities_ref import AllAuthoritiesRef
from netex.all_modes_enumeration import AllModesEnumeration
from netex.all_operators_ref import AllOperatorsRef
from netex.all_organisations_ref import AllOrganisationsRef
from netex.all_public_transport_organisations_ref import AllPublicTransportOrganisationsRef
from netex.all_transport_organisations_ref import AllTransportOrganisationsRef
from netex.assistance_booking_service_ref import AssistanceBookingServiceRef
from netex.assistance_service_ref import AssistanceServiceRef
from netex.authority_ref import AuthorityRef
from netex.boarding_position_ref import BoardingPositionRef
from netex.car_model_profile_ref import CarModelProfileRef
from netex.car_pooling_service_ref import CarPoolingServiceRef
from netex.catering_service_ref import CateringServiceRef
from netex.charging_moment_ref import ChargingMomentRef
from netex.chauffeured_vehicle_service_ref import ChauffeuredVehicleServiceRef
from netex.class_of_use_ref import ClassOfUseRef
from netex.communication_service_ref import CommunicationServiceRef
from netex.complaints_service_ref import ComplaintsServiceRef
from netex.compound_train_ref import CompoundTrainRef
from netex.customer_service_ref import CustomerServiceRef
from netex.cycle_model_profile_ref import CycleModelProfileRef
from netex.discounting_rule_ref import DiscountingRuleRef
from netex.distribution_channel_ref import DistributionChannelRef
from netex.entrance_ref import EntranceRef
from netex.facility_set_ref import FacilitySetRef
from netex.fare_class_enumeration import FareClassEnumeration
from netex.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from netex.fare_section_ref import FareSectionRef
from netex.fare_zone_ref import FareZoneRef
from netex.flexible_line_ref import FlexibleLineRef
from netex.flexible_mode_of_operation_ref import FlexibleModeOfOperationRef
from netex.fulfilment_method_ref import FulfilmentMethodRef
from netex.general_organisation_ref import GeneralOrganisationRef
from netex.group_of_distribution_channels_ref import GroupOfDistributionChannelsRef
from netex.group_of_lines_ref import GroupOfLinesRef
from netex.group_of_operators_ref import GroupOfOperatorsRef
from netex.group_of_services_ref import GroupOfServicesRef
from netex.group_of_single_journeys_ref import GroupOfSingleJourneysRef
from netex.hire_service_ref import HireServiceRef
from netex.left_luggage_service_ref import LeftLuggageServiceRef
from netex.limiting_rule_ref import LimitingRuleRef
from netex.line_ref import LineRef
from netex.local_service_ref import LocalServiceRef
from netex.lost_property_service_ref import LostPropertyServiceRef
from netex.luggage_service_ref import LuggageServiceRef
from netex.management_agent_ref import ManagementAgentRef
from netex.meeting_point_service_ref import MeetingPointServiceRef
from netex.mobility_service_constraint_zone_ref import MobilityServiceConstraintZoneRef
from netex.money_service_ref import MoneyServiceRef
from netex.monitored_vehicle_sharing_parking_bay_ref import MonitoredVehicleSharingParkingBayRef
from netex.network_ref import NetworkRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.online_service_operator_ref import OnlineServiceOperatorRef
from netex.online_service_ref import OnlineServiceRef
from netex.operator_ref import OperatorRef
from netex.organisation_ref import OrganisationRef
from netex.other_organisation_ref import OtherOrganisationRef
from netex.parking_area_ref import ParkingAreaRef
from netex.parking_bay_ref import ParkingBayRef
from netex.parking_entrance_for_vehicles_ref import ParkingEntranceForVehiclesRef
from netex.parking_entrance_ref import ParkingEntranceRef
from netex.parking_passenger_entrance_ref import ParkingPassengerEntranceRef
from netex.parking_ref import ParkingRef
from netex.passenger_seat_ref import PassengerSeatRef
from netex.personal_mode_of_operation_ref import PersonalModeOfOperationRef
from netex.place_use_enumeration import PlaceUseEnumeration
from netex.point_of_interest_classification_ref import PointOfInterestClassificationRef
from netex.point_of_interest_entrance_ref import PointOfInterestEntranceRef
from netex.point_of_interest_ref import PointOfInterestRef
from netex.point_of_interest_space_ref import PointOfInterestSpaceRef
from netex.point_of_interest_vehicle_entrance_ref import PointOfInterestVehicleEntranceRef
from netex.postal_address_ref import PostalAddressRef
from netex.pricing_rule_ref import PricingRuleRef
from netex.quay_ref import QuayRef
from netex.relative_direction_enumeration import RelativeDirectionEnumeration
from netex.retail_consortium_ref import RetailConsortiumRef
from netex.retail_service_ref import RetailServiceRef
from netex.road_address_ref import RoadAddressRef
from netex.routing_type_enumeration import RoutingTypeEnumeration
from netex.scheduled_mode_of_operation_ref import ScheduledModeOfOperationRef
from netex.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.series_constraint_ref import SeriesConstraintRef
from netex.service_facility_set_ref import ServiceFacilitySetRef
from netex.service_journey_pattern_ref import ServiceJourneyPatternRef
from netex.service_journey_ref import ServiceJourneyRef
from netex.service_site_ref import ServiceSiteRef
from netex.serviced_organisation_ref import ServicedOrganisationRef
from netex.simple_vehicle_type_ref import SimpleVehicleTypeRef
from netex.single_journey_path_ref import SingleJourneyPathRef
from netex.single_journey_ref import SingleJourneyRef
from netex.site_component_ref import SiteComponentRef
from netex.site_element_ref import SiteElementRef
from netex.site_facility_set_ref import SiteFacilitySetRef
from netex.site_ref import SiteRef
from netex.stop_place_entrance_ref import StopPlaceEntranceRef
from netex.stop_place_ref import StopPlaceRef
from netex.stop_place_space_ref import StopPlaceSpaceRef
from netex.stop_place_vehicle_entrance_ref import StopPlaceVehicleEntranceRef
from netex.tariff_zone_ref import TariffZoneRef
from netex.taxi_parking_area_ref import TaxiParkingAreaRef
from netex.taxi_rank_ref import TaxiRankRef
from netex.taxi_service_ref import TaxiServiceRef
from netex.taxi_stand_ref import TaxiStandRef
from netex.template_service_journey_ref import TemplateServiceJourneyRef
from netex.ticketing_service_ref import TicketingServiceRef
from netex.topographic_place_ref import TopographicPlaceRef
from netex.train_component_label_assignment_ref import TrainComponentLabelAssignmentRef
from netex.train_element_ref import TrainElementRef
from netex.train_number_ref import TrainNumberRef
from netex.train_ref import TrainRef
from netex.transport_submode import TransportSubmode
from netex.transport_type_ref import TransportTypeRef
from netex.travel_agent_ref import TravelAgentRef
from netex.type_of_concession_ref import TypeOfConcessionRef
from netex.type_of_fare_product_ref import TypeOfFareProductRef
from netex.type_of_fare_structure_element_ref import TypeOfFareStructureElementRef
from netex.type_of_fare_structure_factor_ref import TypeOfFareStructureFactorRef
from netex.type_of_line_ref import TypeOfLineRef
from netex.type_of_machine_readability_ref import TypeOfMachineReadabilityRef
from netex.type_of_payment_method_ref import TypeOfPaymentMethodRef
from netex.type_of_pricing_rule_ref import TypeOfPricingRuleRef
from netex.type_of_product_category_ref import TypeOfProductCategoryRef
from netex.type_of_sales_offer_package_ref import TypeOfSalesOfferPackageRef
from netex.type_of_service_ref import TypeOfServiceRef
from netex.type_of_tariff_ref import TypeOfTariffRef
from netex.type_of_travel_document_ref import TypeOfTravelDocumentRef
from netex.type_of_usage_parameter_ref import TypeOfUsageParameterRef
from netex.vehicle_entrance_ref import VehicleEntranceRef
from netex.vehicle_meeting_link_ref import VehicleMeetingLinkRef
from netex.vehicle_meeting_place_ref import VehicleMeetingPlaceRef
from netex.vehicle_meeting_point_ref import VehicleMeetingPointRef
from netex.vehicle_mode_enumeration import VehicleModeEnumeration
from netex.vehicle_model_ref import VehicleModelRef
from netex.vehicle_pooling_meeting_place_ref import VehiclePoolingMeetingPlaceRef
from netex.vehicle_pooling_parking_area_ref import VehiclePoolingParkingAreaRef
from netex.vehicle_pooling_parking_bay_ref import VehiclePoolingParkingBayRef
from netex.vehicle_pooling_ref import VehiclePoolingRef
from netex.vehicle_ref import VehicleRef
from netex.vehicle_rental_ref import VehicleRentalRef
from netex.vehicle_rental_service_ref import VehicleRentalServiceRef
from netex.vehicle_sharing_parking_area_ref import VehicleSharingParkingAreaRef
from netex.vehicle_sharing_parking_bay_ref import VehicleSharingParkingBayRef
from netex.vehicle_sharing_ref import VehicleSharingRef
from netex.vehicle_sharing_service_ref import VehicleSharingServiceRef
from netex.vehicle_stopping_place_ref import VehicleStoppingPlaceRef
from netex.vehicle_stopping_position_ref import VehicleStoppingPositionRef
from netex.vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ValidityParametersRelStructure(OneToManyRelationshipStructure):
    """
    One to many Relationship for scoping validity parameters.

    :ivar vehicle_modes_or_transport_modes:
    :ivar transport_submode:
    :ivar choice:
    :ivar group_of_operators_ref:
    :ivar choice_1:
    :ivar network_ref_or_group_of_lines_ref:
    :ivar flexible_line_ref_or_line_ref:
    :ivar type_of_line_ref:
    :ivar tariff_zone_ref:
    :ivar fare_zone_ref:
    :ivar fare_section_ref:
    :ivar fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref:
    :ivar vehicle_meeting_point_ref:
    :ivar vehicle_meeting_link_ref:
    :ivar
        vehicle_pooling_meeting_place_ref_or_vehicle_meeting_place_ref:
    :ivar place_use: Use of PLACE.
    :ivar topographic_place_ref:
    :ivar postal_address_ref_or_road_address_ref_or_address_ref:
    :ivar choice_2:
    :ivar point_of_interest_classification_ref:
    :ivar mobility_service_constraint_zone_ref:
    :ivar routing_type: Whether this is a direct i.e. no changes
        required point to point or indirect.
    :ivar directions: Whether use SERIES, or FARE SECTION in forwards,
        backwards or both directions.
    :ivar series_constraint_ref:
    :ivar service_journey_pattern_ref:
    :ivar single_journey_path_ref:
    :ivar class_of_use_ref:
    :ivar fare_class:
    :ivar
        service_facility_set_ref_or_site_facility_set_ref_or_facility_set_ref:
    :ivar type_of_product_category_ref:
    :ivar template_service_journey_ref_or_service_journey_ref:
    :ivar train_number_ref:
    :ivar group_of_services_ref:
    :ivar single_journey_ref:
    :ivar group_of_single_journeys_ref:
    :ivar choice_3:
    :ivar vehicle_model_ref:
    :ivar type_of_service_ref:
    :ivar cycle_model_profile_ref_or_car_model_profile_ref:
    :ivar choice_4:
    :ivar train_element_ref:
    :ivar train_component_label_assignment_ref:
    :ivar passenger_seat_ref:
    :ivar vehicle_ref:
    :ivar type_of_fare_structure_factor_ref:
    :ivar type_of_fare_structure_element_ref:
    :ivar type_of_tariff_ref:
    :ivar limiting_rule_ref_or_discounting_rule_ref_or_pricing_rule_ref:
    :ivar type_of_pricing_rule_ref:
    :ivar charging_moment_ref:
    :ivar type_of_fare_product_ref:
    :ivar type_of_usage_parameter_ref:
    :ivar type_of_concession_ref:
    :ivar type_of_sales_offer_package_ref:
    :ivar type_of_travel_document_ref:
    :ivar type_of_machine_readability_ref:
    :ivar
        distribution_channel_ref_or_group_of_distribution_channels_ref:
    :ivar fulfilment_method_ref:
    :ivar type_of_payment_method_ref:
    """
    class Meta:
        name = "validityParameters_RelStructure"

    vehicle_modes_or_transport_modes: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleModes",
                    "type": List[VehicleModeEnumeration],
                    "namespace": "http://www.netex.org.uk/netex",
                    "default_factory": list,
                    "tokens": True,
                },
                {
                    "name": "TransportModes",
                    "type": List[AllModesEnumeration],
                    "namespace": "http://www.netex.org.uk/netex",
                    "default_factory": list,
                    "tokens": True,
                },
            ),
        }
    )
    transport_submode: List[TransportSubmode] = field(
        default_factory=list,
        metadata={
            "name": "TransportSubmode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    choice: List[object] = field(
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
        }
    )
    group_of_operators_ref: List[GroupOfOperatorsRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfOperatorsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    choice_1: List[object] = field(
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
        }
    )
    network_ref_or_group_of_lines_ref: List[object] = field(
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
        }
    )
    flexible_line_ref_or_line_ref: List[object] = field(
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
        }
    )
    type_of_line_ref: List[TypeOfLineRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfLineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    tariff_zone_ref: List[TariffZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "TariffZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    fare_zone_ref: List[FareZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "FareZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    fare_section_ref: List[FareSectionRef] = field(
        default_factory=list,
        metadata={
            "name": "FareSectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref: List[object] = field(
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
        }
    )
    vehicle_meeting_point_ref: List[VehicleMeetingPointRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleMeetingPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    vehicle_meeting_link_ref: List[VehicleMeetingLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleMeetingLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    vehicle_pooling_meeting_place_ref_or_vehicle_meeting_place_ref: List[object] = field(
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
        }
    )
    place_use: List[PlaceUseEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PlaceUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    topographic_place_ref: List[TopographicPlaceRef] = field(
        default_factory=list,
        metadata={
            "name": "TopographicPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    postal_address_ref_or_road_address_ref_or_address_ref: List[object] = field(
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
        }
    )
    choice_2: List[object] = field(
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
            ),
        }
    )
    point_of_interest_classification_ref: List[PointOfInterestClassificationRef] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestClassificationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    mobility_service_constraint_zone_ref: List[MobilityServiceConstraintZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "MobilityServiceConstraintZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    routing_type: List[RoutingTypeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "RoutingType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    directions: List[RelativeDirectionEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "Directions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    series_constraint_ref: List[SeriesConstraintRef] = field(
        default_factory=list,
        metadata={
            "name": "SeriesConstraintRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    service_journey_pattern_ref: List[ServiceJourneyPatternRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    single_journey_path_ref: List[SingleJourneyPathRef] = field(
        default_factory=list,
        metadata={
            "name": "SingleJourneyPathRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    class_of_use_ref: List[ClassOfUseRef] = field(
        default_factory=list,
        metadata={
            "name": "ClassOfUseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    fare_class: List[FareClassEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "FareClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    service_facility_set_ref_or_site_facility_set_ref_or_facility_set_ref: List[object] = field(
        default_factory=list,
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
    type_of_product_category_ref: List[TypeOfProductCategoryRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfProductCategoryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    template_service_journey_ref_or_service_journey_ref: List[object] = field(
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
        }
    )
    train_number_ref: List[TrainNumberRef] = field(
        default_factory=list,
        metadata={
            "name": "TrainNumberRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    group_of_services_ref: List[GroupOfServicesRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfServicesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    single_journey_ref: List[SingleJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "SingleJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    group_of_single_journeys_ref: List[GroupOfSingleJourneysRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfSingleJourneysRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    choice_3: List[object] = field(
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
    vehicle_model_ref: List[VehicleModelRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleModelRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    type_of_service_ref: List[TypeOfServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    cycle_model_profile_ref_or_car_model_profile_ref: List[object] = field(
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
        }
    )
    choice_4: List[object] = field(
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
                {
                    "name": "LocalServiceRef",
                    "type": LocalServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    train_element_ref: List[TrainElementRef] = field(
        default_factory=list,
        metadata={
            "name": "TrainElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    train_component_label_assignment_ref: List[TrainComponentLabelAssignmentRef] = field(
        default_factory=list,
        metadata={
            "name": "TrainComponentLabelAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    passenger_seat_ref: List[PassengerSeatRef] = field(
        default_factory=list,
        metadata={
            "name": "PassengerSeatRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    vehicle_ref: List[VehicleRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    type_of_fare_structure_factor_ref: List[TypeOfFareStructureFactorRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareStructureFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    type_of_fare_structure_element_ref: List[TypeOfFareStructureElementRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareStructureElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    type_of_tariff_ref: List[TypeOfTariffRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfTariffRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    limiting_rule_ref_or_discounting_rule_ref_or_pricing_rule_ref: List[object] = field(
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
        }
    )
    type_of_pricing_rule_ref: List[TypeOfPricingRuleRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPricingRuleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    charging_moment_ref: List[ChargingMomentRef] = field(
        default_factory=list,
        metadata={
            "name": "ChargingMomentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    type_of_fare_product_ref: List[TypeOfFareProductRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    type_of_usage_parameter_ref: List[TypeOfUsageParameterRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfUsageParameterRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    type_of_concession_ref: List[TypeOfConcessionRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfConcessionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    type_of_sales_offer_package_ref: List[TypeOfSalesOfferPackageRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfSalesOfferPackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    type_of_travel_document_ref: List[TypeOfTravelDocumentRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfTravelDocumentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    type_of_machine_readability_ref: List[TypeOfMachineReadabilityRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfMachineReadabilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    distribution_channel_ref_or_group_of_distribution_channels_ref: List[object] = field(
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
        }
    )
    fulfilment_method_ref: List[FulfilmentMethodRef] = field(
        default_factory=list,
        metadata={
            "name": "FulfilmentMethodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
    type_of_payment_method_ref: List[TypeOfPaymentMethodRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPaymentMethodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "sequence": 1,
        }
    )
