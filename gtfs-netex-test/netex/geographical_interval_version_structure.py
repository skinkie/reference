from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.fare_interval_version_structure import FareIntervalVersionStructure
from netex.geographical_interval_prices_rel_structure import GeographicalIntervalPricesRelStructure
from netex.geographical_unit_ref import GeographicalUnitRef
from netex.interval_type_enumeration import IntervalTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GeographicalIntervalVersionStructure(FareIntervalVersionStructure):
    """
    Type for GEOGRAPHICAL INTERVAL.

    :ivar start_geographical_value: Start value for Geographic Interval.
    :ivar end_geographical_value: End value for Geographic Interval.
    :ivar number_of_units: Number of units in Interval.
    :ivar interval_type: nature of Interval.
    :ivar geographical_unit_ref:
    :ivar prices: PRICEs of GEOGRAPHICAL INTERVAL.
    """
    class Meta:
        name = "GeographicalInterval_VersionStructure"

    start_geographical_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "StartGeographicalValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_geographical_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "EndGeographicalValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    number_of_units: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfUnits",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    interval_type: Optional[IntervalTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "IntervalType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_unit_ref: Optional[GeographicalUnitRef] = field(
        default=None,
        metadata={
            "name": "GeographicalUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    prices: Optional[GeographicalIntervalPricesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
