from dataclasses import dataclass, field
from typing import Optional
from netex.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.derived_view_structure import DerivedViewStructure
from netex.multilingual_string import MultilingualString
from netex.network_ref import NetworkRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class NetworkDerivedViewStructure(DerivedViewStructure):
    """
    Type for a NETWORK VIEW.

    :ivar network_ref:
    :ivar name: Name of NETWORK.
    :ivar transport_mode: TRANSPORT MODE of NETWORK.
    """
    class Meta:
        name = "Network_DerivedViewStructure"

    network_ref: Optional[NetworkRef] = field(
        default=None,
        metadata={
            "name": "NetworkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
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
