from dataclasses import dataclass, field
from typing import Union

from .branding import Branding
from .charging_moment import ChargingMoment
from .class_of_use import ClassOfUse
from .customer_account_status import CustomerAccountStatus
from .data_source import DataSource
from .direction import Direction
from .open_transport_mode import OpenTransportMode
from .parking_bay_status import ParkingBayStatus
from .point_of_interest_classification import PointOfInterestClassification
from .price_unit import PriceUnit
from .purpose_of_equipment_profile import PurposeOfEquipmentProfile
from .purpose_of_grouping import PurposeOfGrouping
from .purpose_of_journey_partition import PurposeOfJourneyPartition
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from .submode import Submode
from .timing_algorithm_type import TimingAlgorithmType
from .type_of_access_right_assignment import TypeOfAccessRightAssignment
from .type_of_activation import TypeOfActivation
from .type_of_battery_chemistry import TypeOfBatteryChemistry
from .type_of_codespace_assignment import TypeOfCodespaceAssignment
from .type_of_concession import TypeOfConcession
from .type_of_congestion import TypeOfCongestion
from .type_of_customer_account import TypeOfCustomerAccount
from .type_of_deck_entrance import TypeOfDeckEntrance
from .type_of_deck_space import TypeOfDeckSpace
from .type_of_delivery_variant import TypeOfDeliveryVariant
from .type_of_driver_permit import TypeOfDriverPermit
from .type_of_entity import TypeOfEntity
from .type_of_equipment import TypeOfEquipment
from .type_of_facility import TypeOfFacility
from .type_of_fare_contract import TypeOfFareContract
from .type_of_fare_contract_entry import TypeOfFareContractEntry
from .type_of_fare_product import TypeOfFareProduct
from .type_of_fare_structure_element import TypeOfFareStructureElement
from .type_of_fare_structure_factor import TypeOfFareStructureFactor
from .type_of_fare_table import TypeOfFareTable
from .type_of_feature import TypeOfFeature
from .type_of_fleet import TypeOfFleet
from .type_of_flexible_service import TypeOfFlexibleService
from .type_of_journey_pattern import TypeOfJourneyPattern
from .type_of_line import TypeOfLine
from .type_of_link import TypeOfLink
from .type_of_link_sequence import TypeOfLinkSequence
from .type_of_locatable_spot import TypeOfLocatableSpot
from .type_of_machine_readability import TypeOfMachineReadability
from .type_of_medium_access_device import TypeOfMediumAccessDevice
from .type_of_mobility_service import TypeOfMobilityService
from .type_of_mode_of_operation import TypeOfModeOfOperation
from .type_of_notice import TypeOfNotice
from .type_of_operation import TypeOfOperation
from .type_of_organisation import TypeOfOrganisation
from .type_of_organisation_part import TypeOfOrganisationPart
from .type_of_parking import TypeOfParking
from .type_of_passenger_information_equipment import TypeOfPassengerInformationEquipment
from .type_of_payment_method import TypeOfPaymentMethod
from .type_of_place import TypeOfPlace
from .type_of_plug import TypeOfPlug
from .type_of_point import TypeOfPoint
from .type_of_pricing_rule import TypeOfPricingRule
from .type_of_product_category import TypeOfProductCategory
from .type_of_projection import TypeOfProjection
from .type_of_proof import TypeOfProof
from .type_of_responsibility_role import TypeOfResponsibilityRole
from .type_of_retail_device import TypeOfRetailDevice
from .type_of_rolling_stock import TypeOfRollingStock
from .type_of_sales_offer_package import TypeOfSalesOfferPackage
from .type_of_security_list import TypeOfSecurityList
from .type_of_service import TypeOfService
from .type_of_service_feature import TypeOfServiceFeature
from .type_of_tariff import TypeOfTariff
from .type_of_time_demand_type import TypeOfTimeDemandType
from .type_of_transfer import TypeOfTransfer
from .type_of_travel_document import TypeOfTravelDocument
from .type_of_usage_parameter import TypeOfUsageParameter
from .type_of_validity import TypeOfValidity
from .type_of_version import TypeOfVersion
from .type_of_zone import TypeOfZone
from .types_of_frame_rel_structure import TypeOfFrame

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypesOfValueStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "typesOfValueStructure"

    type_of_value_or_type_of_entity: list[
        Union[
            ParkingBayStatus,
            TypeOfMediumAccessDevice,
            TypeOfMachineReadability,
            TypeOfProof,
            TypeOfConcession,
            ChargingMoment,
            TypeOfUsageParameter,
            TypeOfFareTable,
            TypeOfPricingRule,
            PriceUnit,
            TimingAlgorithmType,
            PurposeOfJourneyPartition,
            PointOfInterestClassification,
            TypeOfParking,
            TypeOfServiceFeature,
            Direction,
            TypeOfFleet,
            TypeOfDeckEntrance,
            TypeOfDeckSpace,
            TypeOfLocatableSpot,
            TypeOfSecurityList,
            TypeOfDriverPermit,
            PurposeOfEquipmentProfile,
            TypeOfProductCategory,
            TypeOfPaymentMethod,
            ClassOfUse,
            Submode,
            OpenTransportMode,
            TypeOfValidity,
            TypeOfCodespaceAssignment,
            PurposeOfGrouping,
            Branding,
            DataSource,
            TypeOfMobilityService,
            TypeOfRetailDevice,
            CustomerAccountStatus,
            TypeOfCustomerAccount,
            TypeOfFareContractEntry,
            TypeOfFareContract,
            TypeOfTravelDocument,
            TypeOfSalesOfferPackage,
            TypeOfFareProduct,
            TypeOfFareStructureElement,
            TypeOfTariff,
            TypeOfAccessRightAssignment,
            TypeOfFareStructureFactor,
            TypeOfFlexibleService,
            TypeOfTimeDemandType,
            TypeOfPassengerInformationEquipment,
            TypeOfJourneyPattern,
            TypeOfActivation,
            TypeOfRollingStock,
            TypeOfModeOfOperation,
            TypeOfPlug,
            TypeOfBatteryChemistry,
            TypeOfLine,
            TypeOfDeliveryVariant,
            TypeOfNotice,
            TypeOfCongestion,
            TypeOfFacility,
            TypeOfService,
            TypeOfEquipment,
            TypeOfFeature,
            TypeOfLinkSequence,
            TypeOfPlace,
            TypeOfTransfer,
            TypeOfFrame,
            TypeOfResponsibilityRole,
            TypeOfOperation,
            TypeOfOrganisationPart,
            TypeOfOrganisation,
            TypeOfZone,
            TypeOfLink,
            TypeOfPoint,
            TypeOfProjection,
            TypeOfEntity,
            TypeOfVersion,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ParkingBayStatus",
                    "type": ParkingBayStatus,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfMediumAccessDevice",
                    "type": TypeOfMediumAccessDevice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfMachineReadability",
                    "type": TypeOfMachineReadability,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfProof",
                    "type": TypeOfProof,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfConcession",
                    "type": TypeOfConcession,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChargingMoment",
                    "type": ChargingMoment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfUsageParameter",
                    "type": TypeOfUsageParameter,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareTable",
                    "type": TypeOfFareTable,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPricingRule",
                    "type": TypeOfPricingRule,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PriceUnit",
                    "type": PriceUnit,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingAlgorithmType",
                    "type": TimingAlgorithmType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PurposeOfJourneyPartition",
                    "type": PurposeOfJourneyPartition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestClassification",
                    "type": PointOfInterestClassification,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfParking",
                    "type": TypeOfParking,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfServiceFeature",
                    "type": TypeOfServiceFeature,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Direction",
                    "type": Direction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFleet",
                    "type": TypeOfFleet,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfDeckEntrance",
                    "type": TypeOfDeckEntrance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfDeckSpace",
                    "type": TypeOfDeckSpace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfLocatableSpot",
                    "type": TypeOfLocatableSpot,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfSecurityList",
                    "type": TypeOfSecurityList,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfDriverPermit",
                    "type": TypeOfDriverPermit,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PurposeOfEquipmentProfile",
                    "type": PurposeOfEquipmentProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfProductCategory",
                    "type": TypeOfProductCategory,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPaymentMethod",
                    "type": TypeOfPaymentMethod,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ClassOfUse",
                    "type": ClassOfUse,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Submode",
                    "type": Submode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OpenTransportMode",
                    "type": OpenTransportMode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfValidity",
                    "type": TypeOfValidity,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfCodespaceAssignment",
                    "type": TypeOfCodespaceAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PurposeOfGrouping",
                    "type": PurposeOfGrouping,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Branding",
                    "type": Branding,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DataSource",
                    "type": DataSource,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfMobilityService",
                    "type": TypeOfMobilityService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfRetailDevice",
                    "type": TypeOfRetailDevice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerAccountStatus",
                    "type": CustomerAccountStatus,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfCustomerAccount",
                    "type": TypeOfCustomerAccount,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareContractEntry",
                    "type": TypeOfFareContractEntry,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareContract",
                    "type": TypeOfFareContract,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTravelDocument",
                    "type": TypeOfTravelDocument,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfSalesOfferPackage",
                    "type": TypeOfSalesOfferPackage,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareProduct",
                    "type": TypeOfFareProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareStructureElement",
                    "type": TypeOfFareStructureElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTariff",
                    "type": TypeOfTariff,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfAccessRightAssignment",
                    "type": TypeOfAccessRightAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareStructureFactor",
                    "type": TypeOfFareStructureFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFlexibleService",
                    "type": TypeOfFlexibleService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTimeDemandType",
                    "type": TypeOfTimeDemandType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPassengerInformationEquipment",
                    "type": TypeOfPassengerInformationEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfJourneyPattern",
                    "type": TypeOfJourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfActivation",
                    "type": TypeOfActivation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfRollingStock",
                    "type": TypeOfRollingStock,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfModeOfOperation",
                    "type": TypeOfModeOfOperation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPlug",
                    "type": TypeOfPlug,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfBatteryChemistry",
                    "type": TypeOfBatteryChemistry,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfLine",
                    "type": TypeOfLine,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfDeliveryVariant",
                    "type": TypeOfDeliveryVariant,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfNotice",
                    "type": TypeOfNotice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfCongestion",
                    "type": TypeOfCongestion,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFacility",
                    "type": TypeOfFacility,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfService",
                    "type": TypeOfService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfEquipment",
                    "type": TypeOfEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFeature",
                    "type": TypeOfFeature,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfLinkSequence",
                    "type": TypeOfLinkSequence,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPlace",
                    "type": TypeOfPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTransfer",
                    "type": TypeOfTransfer,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFrame",
                    "type": TypeOfFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfResponsibilityRole",
                    "type": TypeOfResponsibilityRole,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfOperation",
                    "type": TypeOfOperation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfOrganisationPart",
                    "type": TypeOfOrganisationPart,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfOrganisation",
                    "type": TypeOfOrganisation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfZone",
                    "type": TypeOfZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfLink",
                    "type": TypeOfLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPoint",
                    "type": TypeOfPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfProjection",
                    "type": TypeOfProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfEntity",
                    "type": TypeOfEntity,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfVersion",
                    "type": TypeOfVersion,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
