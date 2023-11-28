from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.cell_versioned_child_structure import PriceableObjectVersionStructure
from netex.distance_matrix_element_prices_rel_structure import DistanceMatrixElementPricesRelStructure
from netex.fare_point_in_pattern_ref_structure import FarePointInPatternRefStructure
from netex.fare_section_ref_structure import FareSectionRefStructure
from netex.fare_table_ref import FareTableRef
from netex.geographical_structure_factors_rel_structure import GeographicalStructureFactorsRelStructure
from netex.point_ref_structure import PointRefStructure
from netex.scheduled_stop_point_derived_view_structure import ScheduledStopPointDerivedViewStructure
from netex.scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from netex.series_constraints_rel_structure import SeriesConstraintsRelStructure
from netex.standard_fare_table_ref import StandardFareTableRef
from netex.tariff_refs_rel_structure import TariffRefsRelStructure
from netex.tariff_zone_ref_structure import TariffZoneRefStructure
from netex.zone_derived_view_structure import ZoneDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DistanceMatrixElementVersionStructure(PriceableObjectVersionStructure):
    """
    Type for DISTANCE MATRIX ELEMENT.

    :ivar distance: DISTANCE MATRIX ELEMENT to use when advertising
        Train -If different from Id.
    :ivar relative_ranking: Relative preference assigned to this element
        if there are multiple entries between two points.
    :ivar is_direct: Whether considered as direct fare.
    :ivar inverse_allowed: Whether an inverse element in the opposite
        direction can be assumed with the same prices. (Optimisation to
        reduce  data exchanged)
    :ivar choice:
    :ivar choice_1:
    :ivar series_constraints: SERIES CONSTRAINTs constraining DISTANCE
        MATRIX ELEMENT.
    :ivar structure_factors: Use of FARE STRUCTURE ELEMENTs in a
        particular sequence.
    :ivar tariffs: TARIFFs applying to element.
    :ivar standard_fare_table_ref_or_fare_table_ref:
    :ivar prices: prices associated with DSISTANCE MATRIX ELEMENT.
    """
    class Meta:
        name = "DistanceMatrixElement_VersionStructure"

    distance: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    relative_ranking: Optional[int] = field(
        default=None,
        metadata={
            "name": "RelativeRanking",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    is_direct: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsDirect",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    inverse_allowed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InverseAllowed",
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
                    "name": "StartStopPointRef",
                    "type": ScheduledStopPointRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StartStopPointView",
                    "type": ScheduledStopPointDerivedViewStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StartTariffZoneRef",
                    "type": TariffZoneRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StartTariffZoneView",
                    "type": ZoneDerivedViewStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StartMeetingPointRef",
                    "type": PointRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FromFareSectionRef",
                    "type": FareSectionRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FromFarePointInPatternRef",
                    "type": FarePointInPatternRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    choice_1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "EndStopPointRef",
                    "type": ScheduledStopPointRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EndStopPointView",
                    "type": ScheduledStopPointDerivedViewStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EndTariffZoneRef",
                    "type": TariffZoneRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EndTariffZoneView",
                    "type": ZoneDerivedViewStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EndMeetingPointRef",
                    "type": PointRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ToFareSectionRef",
                    "type": FareSectionRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ToFarePointInPatternRef",
                    "type": FarePointInPatternRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    series_constraints: Optional[SeriesConstraintsRelStructure] = field(
        default=None,
        metadata={
            "name": "seriesConstraints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    structure_factors: Optional[GeographicalStructureFactorsRelStructure] = field(
        default=None,
        metadata={
            "name": "structureFactors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tariffs: Optional[TariffRefsRelStructure] = field(
        default=None,
        metadata={
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
    prices: Optional[DistanceMatrixElementPricesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
