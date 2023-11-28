from dataclasses import dataclass, field
from typing import List
from netex.all_distribution_channels_ref import AllDistributionChannelsRef
from netex.customer_account_status_ref import CustomerAccountStatusRef
from netex.flexible_mode_of_operation_ref import FlexibleModeOfOperationRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.personal_mode_of_operation_ref import PersonalModeOfOperationRef
from netex.scheduled_mode_of_operation_ref import ScheduledModeOfOperationRef
from netex.type_of_access_right_assignment_ref import TypeOfAccessRightAssignmentRef
from netex.type_of_battery_chemistry_ref import TypeOfBatteryChemistryRef
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
from netex.type_of_feature_ref import TypeOfFeatureRef
from netex.type_of_flexible_service_ref import TypeOfFlexibleServiceRef
from netex.type_of_frame_ref import TypeOfFrameRef
from netex.type_of_journey_pattern_ref import TypeOfJourneyPatternRef
from netex.type_of_line_ref import TypeOfLineRef
from netex.type_of_link_ref import TypeOfLinkRef
from netex.type_of_link_sequence_ref import TypeOfLinkSequenceRef
from netex.type_of_machine_readability_ref import TypeOfMachineReadabilityRef
from netex.type_of_mobility_service_ref import TypeOfMobilityServiceRef
from netex.type_of_mode_of_operation_ref import TypeOfModeOfOperationRef
from netex.type_of_notice_ref import TypeOfNoticeRef
from netex.type_of_organisation_part_ref import TypeOfOrganisationPartRef
from netex.type_of_organisation_ref import TypeOfOrganisationRef
from netex.type_of_passenger_information_equipment_ref import TypeOfPassengerInformationEquipmentRef
from netex.type_of_place_ref import TypeOfPlaceRef
from netex.type_of_plug_ref import TypeOfPlugRef
from netex.type_of_point_ref import TypeOfPointRef
from netex.type_of_pricing_rule_ref import TypeOfPricingRuleRef
from netex.type_of_projection_ref import TypeOfProjectionRef
from netex.type_of_retail_device_ref import TypeOfRetailDeviceRef
from netex.type_of_sales_offer_package_ref import TypeOfSalesOfferPackageRef
from netex.type_of_security_list_ref import TypeOfSecurityListRef
from netex.type_of_service_feature_ref import TypeOfServiceFeatureRef
from netex.type_of_service_ref import TypeOfServiceRef
from netex.type_of_tariff_ref import TypeOfTariffRef
from netex.type_of_time_demand_type_ref import TypeOfTimeDemandTypeRef
from netex.type_of_transfer_ref import TypeOfTransferRef
from netex.type_of_travel_document_ref import TypeOfTravelDocumentRef
from netex.type_of_validity_ref import TypeOfValidityRef
from netex.type_of_zone_ref import TypeOfZoneRef
from netex.vehicle_pooling_ref import VehiclePoolingRef
from netex.vehicle_rental_ref import VehicleRentalRef
from netex.vehicle_sharing_ref import VehicleSharingRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfEntityRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of references to a TYPE OF VALUE.
    """
    class Meta:
        name = "typeOfEntityRefs_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
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
            ),
        }
    )
