from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from netex.cell_versioned_child_structure import PriceableObjectVersionStructure
from netex.connection_ref_structure import ConnectionRefStructure
from netex.fare_basis_enumeration import FareBasisEnumeration
from netex.fare_points_in_pattern_rel_structure import FarePointsInPatternRelStructure
from netex.journey_pattern_refs_rel_structure import JourneyPatternRefsRelStructure
from netex.multilingual_string import MultilingualString
from netex.private_code import PrivateCode
from netex.routing_type_enumeration import RoutingTypeEnumeration
from netex.series_constraint_prices_rel_structure import SeriesConstraintPricesRelStructure
from netex.series_constraint_refs_rel_structure import SeriesConstraintRefsRelStructure
from netex.series_type_enumeration import SeriesTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SeriesConstraintVersionStructure(PriceableObjectVersionStructure):
    """
    Type for SERIES CONSTRAINT.

    :ivar private_code:
    :ivar itinerary: String to use to represent Itinerary.
    :ivar symbol_marking_usual_route: Symbal to us eto mark normal
        route.
    :ivar series_type: Classification of SERIES CONSTRAINT. Default is
        station to station.
    :ivar routing_type: Whether this is a direct i.e. no changes
        requried point to point or indirect.
    :ivar fare_basis: Preferred basis for calculating fares for this
        series.
    :ivar first_class_distance: Distance r calculation  of First Class
        fares.
    :ivar second_class_distance: Distance r calculation  of Second Class
        fares.
    :ivar discrete: Whether SERIES CONSTRAINT can only be used by
        itself, or whether it can be used in a chain of series.
    :ivar from_connection_ref: Start CONNECTION link  for   SERIES
        CONSTRAINT.
    :ivar to_connection_ref: End CONNECTION link  for   SERIES
        CONSTRAINT.
    :ivar fare_points_in_pattern: FARE POINTs IN  PATTERN  in the SERIES
        CONSTRAINT.
    :ivar journey_patterns: JourneyPatternsequivalent to the series.
    :ivar prices: Frices for the SERIES CONSTRAINTs  (Needed for TAP
        TSI)
    :ivar replaces: Replaces the speciified SERIES CONSTRAINTs  (Needed
        for TAP TSI)
    :ivar order: relative number of series for same  OD pair (TAP Route
        number)
    """
    class Meta:
        name = "SeriesConstraint_VersionStructure"

    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    itinerary: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Itinerary",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    symbol_marking_usual_route: Optional[str] = field(
        default=None,
        metadata={
            "name": "SymbolMarkingUsualRoute",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    series_type: Optional[SeriesTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "SeriesType",
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
    fare_basis: Optional[FareBasisEnumeration] = field(
        default=None,
        metadata={
            "name": "FareBasis",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    first_class_distance: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FirstClassDistance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    second_class_distance: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SecondClassDistance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    discrete: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Discrete",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    from_connection_ref: Optional[ConnectionRefStructure] = field(
        default=None,
        metadata={
            "name": "FromConnectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    to_connection_ref: Optional[ConnectionRefStructure] = field(
        default=None,
        metadata={
            "name": "ToConnectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_points_in_pattern: List[FarePointsInPatternRelStructure] = field(
        default_factory=list,
        metadata={
            "name": "farePointsInPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_patterns: List[JourneyPatternRefsRelStructure] = field(
        default_factory=list,
        metadata={
            "name": "journeyPatterns",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    prices: List[SeriesConstraintPricesRelStructure] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    replaces: List[SeriesConstraintRefsRelStructure] = field(
        default_factory=list,
        metadata={
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
