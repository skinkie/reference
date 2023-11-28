from dataclasses import dataclass, field
from typing import Optional
from netex.access_right_parameter_assignments_in_frame_rel_structure import AccessRightParameterAssignmentsInFrameRelStructure
from netex.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.authority_ref import AuthorityRef
from netex.border_points_in_frame_rel_structure import BorderPointsInFrameRelStructure
from netex.common_version_frame_structure import CommonVersionFrameStructure
from netex.controllable_elements_in_frame_rel_structure import ControllableElementsInFrameRelStructure
from netex.distance_matrix_elements_rel_structure import DistanceMatrixElementsRelStructure
from netex.distribution_assignments_in_frame_rel_structure import DistributionAssignmentsInFrameRelStructure
from netex.distribution_channels_in_frame_rel_structure import DistributionChannelsInFrameRelStructure
from netex.fare_prices_in_frame_rel_structure import FarePricesInFrameRelStructure
from netex.fare_products_in_frame_rel_structure import FareProductsInFrameRelStructure
from netex.fare_scheduled_stop_points_in_frame_rel_structure import FareScheduledStopPointsInFrameRelStructure
from netex.fare_sections_in_frame_rel_structure import FareSectionsInFrameRelStructure
from netex.fare_series_in_frame_rel_structure import FareSeriesInFrameRelStructure
from netex.fare_structure_elements_in_frame_rel_structure import FareStructureElementsInFrameRelStructure
from netex.fare_tables_in_frame_rel_structure import FareTablesInFrameRelStructure
from netex.fare_zones_in_frame_rel_structure import FareZonesInFrameRelStructure
from netex.fulfilment_methods_in_frame_rel_structure import FulfilmentMethodsInFrameRelStructure
from netex.geographical_intervals_rel_structure import GeographicalIntervalsRelStructure
from netex.geographical_structure_factors_rel_structure import GeographicalStructureFactorsRelStructure
from netex.geographical_units_rel_structure import GeographicalUnitsRelStructure
from netex.groups_of_distance_matrix_elements_rel_structure import GroupsOfDistanceMatrixElementsRelStructure
from netex.groups_of_distribution_channels_in_frame_rel_structure import GroupsOfDistributionChannelsInFrameRelStructure
from netex.groups_of_sales_offer_packages_in_frame_rel_structure import GroupsOfSalesOfferPackagesInFrameRelStructure
from netex.notice_assignments_in_frame_rel_structure import NoticeAssignmentsInFrameRelStructure
from netex.notices_in_frame_rel_structure import NoticesInFrameRelStructure
from netex.operator_ref import OperatorRef
from netex.parking_tariffs_in_frame_rel_structure import ParkingTariffsInFrameRelStructure
from netex.pricing_parameter_set import PricingParameterSet
from netex.quality_structure_factors_rel_structure import QualityStructureFactorsRelStructure
from netex.sales_offer_package_elements_in_frame_rel_structure import SalesOfferPackageElementsInFrameRelStructure
from netex.sales_offer_package_substitutions_in_frame_rel_structure import SalesOfferPackageSubstitutionsInFrameRelStructure
from netex.sales_offer_packages_in_frame_rel_structure import SalesOfferPackagesInFrameRelStructure
from netex.tariffs_in_frame_rel_structure import TariffsInFrameRelStructure
from netex.time_intervals_rel_structure import TimeIntervalsRelStructure
from netex.time_structure_factors_rel_structure import TimeStructureFactorsRelStructure
from netex.time_units_rel_structure import TimeUnitsRelStructure
from netex.types_of_travel_document_in_frame_rel_structure import TypesOfTravelDocumentInFrameRelStructure
from netex.usage_parameters_in_frame_rel_structure import UsageParametersInFrameRelStructure
from netex.validable_elements_in_frame_rel_structure import ValidableElementsInFrameRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareFrameVersionFrameStructure(CommonVersionFrameStructure):
    """
    Type for a FARE FRAME.

    :ivar mode: Default TRANSPORT MODE.
    :ivar authority_ref_or_operator_ref:
    :ivar pricing_parameter_set:
    :ivar notices: NOTICEs in frame.
    :ivar notice_assignments: NOTICE ASSIGNMENTs in frame.
    :ivar border_points: BORDER POINTs in FRAME.
    :ivar fare_scheduled_stop_points: FARE SCHEDULED STOP POINTs in
        FRAME.
    :ivar fare_zones: FARE ZONEs in FRAME.
    :ivar fare_sections: FARE SECTIONs in FRAME.
    :ivar series_constraints: FARE PRODUCTs in FRAME.
    :ivar geographical_units: GEOGRAPHICAL UNITs in  Frame.
    :ivar geographical_intervals: GEOGRAPHICAL INTERVALs in  Frame.
    :ivar geographical_structure_factors: GEOGRAPHICAL STRUCTURE FACTORS
        in  Frame.
    :ivar time_units: TIME UNITs in  Frame.
    :ivar time_intervals: TIME INTERVALs in  Frame.
    :ivar time_structure_factors: TIME STRUCTURE FACTORS in  Frame.
    :ivar quality_structure_factors: QUALITY STRUCTURE FACTORS in
        Frame.
    :ivar distance_matrix_elements: DISTANCE MATRIX ELEMENTs in Frame.
    :ivar groups_of_distance_matrix_elements: GROUPs OF DISTANCE MATRIX
        ELEMENTs in Frame.
    :ivar fare_structure_elements: FARE STRUCTURE ELEMENTs in FRAME.
    :ivar tariffs: TARIFFs in FRAME.
    :ivar validable_elements: VALIDABLE ELEMENTs in FRAME.
    :ivar controllable_elements: CONTROLLABLE ELEMENTs in FRAME.
    :ivar usage_parameters: FARE USAGE PARAMETERS in FRAME.
    :ivar access_right_parameter_assignments: ACCESS RIGHT PARAMETER
        ASSIGNMENTs in frame.
    :ivar fare_products: FARE PRODUCTs in FRAME.
    :ivar price_groups: PRICE GROUPs in FRAME.
    :ivar fare_tables: FARE TABLEs in FRAME.
    :ivar distribution_channels: DISTRIBUTION CHANNELS in FRAME.
    :ivar groups_of_distribution_channels: DISTRIBUTION CHANNELS in
        FRAME.
    :ivar fulfilment_methods: FULFILMENT METHODS  in FRAME.
    :ivar types_of_travel_documents: TYPE OF TRAVEL DOCUMENTs in FRAME.
    :ivar sales_offer_packages: SALES OFFER PACKAGEs in FRAME.
    :ivar sales_offer_package_elements: SALES OFFER PACKAGEs in FRAME.
    :ivar sales_offer_package_substitutions: SALES OFFER PACKAGEs in
        FRAME.
    :ivar groups_of_sales_offer_packages: GROUPS OF SALES OFFER PACKAGEs
        in FRAME.
    :ivar distribution_assignments: DISTRIBUTION ASSIGNMENTS in FRAME.
    :ivar parking_tariffs: PARKING TARIFFs in frame.
    """
    class Meta:
        name = "FareFrame_VersionFrameStructure"

    mode: Optional[AllVehicleModesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "Mode",
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
    pricing_parameter_set: Optional[PricingParameterSet] = field(
        default=None,
        metadata={
            "name": "PricingParameterSet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notices: Optional[NoticesInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notice_assignments: Optional[NoticeAssignmentsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    border_points: Optional[BorderPointsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "borderPoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_scheduled_stop_points: Optional[FareScheduledStopPointsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "fareScheduledStopPoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_zones: Optional[FareZonesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "fareZones",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_sections: Optional[FareSectionsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "fareSections",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    series_constraints: Optional[FareSeriesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "seriesConstraints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_units: Optional[GeographicalUnitsRelStructure] = field(
        default=None,
        metadata={
            "name": "geographicalUnits",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_intervals: Optional[GeographicalIntervalsRelStructure] = field(
        default=None,
        metadata={
            "name": "geographicalIntervals",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_structure_factors: Optional[GeographicalStructureFactorsRelStructure] = field(
        default=None,
        metadata={
            "name": "geographicalStructureFactors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_units: Optional[TimeUnitsRelStructure] = field(
        default=None,
        metadata={
            "name": "timeUnits",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_intervals: Optional[TimeIntervalsRelStructure] = field(
        default=None,
        metadata={
            "name": "timeIntervals",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_structure_factors: Optional[TimeStructureFactorsRelStructure] = field(
        default=None,
        metadata={
            "name": "timeStructureFactors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    quality_structure_factors: Optional[QualityStructureFactorsRelStructure] = field(
        default=None,
        metadata={
            "name": "qualityStructureFactors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distance_matrix_elements: Optional[DistanceMatrixElementsRelStructure] = field(
        default=None,
        metadata={
            "name": "distanceMatrixElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    groups_of_distance_matrix_elements: Optional[GroupsOfDistanceMatrixElementsRelStructure] = field(
        default=None,
        metadata={
            "name": "groupsOfDistanceMatrixElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_structure_elements: Optional[FareStructureElementsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "fareStructureElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tariffs: Optional[TariffsInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validable_elements: Optional[ValidableElementsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "validableElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    controllable_elements: Optional[ControllableElementsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "controllableElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    usage_parameters: Optional[UsageParametersInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "usageParameters",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_right_parameter_assignments: Optional[AccessRightParameterAssignmentsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "accessRightParameterAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_products: Optional[FareProductsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "fareProducts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    price_groups: Optional[FarePricesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "priceGroups",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_tables: Optional[FareTablesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "fareTables",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distribution_channels: Optional[DistributionChannelsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "distributionChannels",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    groups_of_distribution_channels: Optional[GroupsOfDistributionChannelsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "groupsOfDistributionChannels",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fulfilment_methods: Optional[FulfilmentMethodsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "fulfilmentMethods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    types_of_travel_documents: Optional[TypesOfTravelDocumentInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "typesOfTravelDocuments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_offer_packages: Optional[SalesOfferPackagesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "salesOfferPackages",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_offer_package_elements: Optional[SalesOfferPackageElementsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "salesOfferPackageElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_offer_package_substitutions: Optional[SalesOfferPackageSubstitutionsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "salesOfferPackageSubstitutions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    groups_of_sales_offer_packages: Optional[GroupsOfSalesOfferPackagesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "groupsOfSalesOfferPackages",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distribution_assignments: Optional[DistributionAssignmentsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "distributionAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_tariffs: Optional[ParkingTariffsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "parkingTariffs",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
