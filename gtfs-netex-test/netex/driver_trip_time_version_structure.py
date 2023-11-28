from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.driver_trip_ref import DriverTripRef
from netex.multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DriverTripTimeVersionStructure(DataManagedObjectStructure):
    """
    Type for DRIVER TRIP TIME.

    :ivar description: Description of DRIVER TRIP TIME.
    :ivar driver_trip_ref:
    :ivar duration: How long the DRIVER TRIP takes.
    :ivar transport_mode: Mode of Transport.
    """
    class Meta:
        name = "DriverTripTime_VersionStructure"

    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    driver_trip_ref: Optional[DriverTripRef] = field(
        default=None,
        metadata={
            "name": "DriverTripRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transport_mode: Optional[AllVehicleModesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
