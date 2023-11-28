from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.driver_trip_times_rel_structure import DriverTripTimesRelStructure
from netex.multilingual_string import MultilingualString
from netex.timing_point_ref_structure import TimingPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DriverTripVersionStructure(DataManagedObjectStructure):
    """
    Type for DRIVER TRIP.

    :ivar description: Description of DRIVER TRIP.
    :ivar start_point_ref: TIMING POINT at which run starts.
    :ivar end_point_ref: TIMING POINT at which run starts.
    :ivar accounting_time: How long the run takes.
    :ivar accounting_factor: How long the run takes to prepare.
    :ivar trip_times: DRIVER TRIP TIMEs for DRIVER TRIP.
    """
    class Meta:
        name = "DriverTrip_VersionStructure"

    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_point_ref: Optional[TimingPointRefStructure] = field(
        default=None,
        metadata={
            "name": "StartPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_point_ref: Optional[TimingPointRefStructure] = field(
        default=None,
        metadata={
            "name": "EndPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    accounting_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "AccountingTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    accounting_factor: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "AccountingFactor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    trip_times: Optional[DriverTripTimesRelStructure] = field(
        default=None,
        metadata={
            "name": "tripTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
